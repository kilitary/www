"""
Python 3.14 version of MQL5 script: Print current positions and apply trailing TP
Using real MetaTrader5 Python API
"""

import math
import sys
import time

import rich
import rich.traceback

import MetaTrader5 as mt5

# Trailing TP parameters
TRAIL_STEP = 145.0
TRAIL_PROFIT_STEP = 50
MIN_PROFIT_POINTS = 45
FREEZE_SL_POINTS = 30
MIN_CURRENT_PROFIT = 2.0
PROFITABLE_SL_STEP = 22
BUY_TRAIL_PROFIT_MULTIPLIER = 1.2
SKIP_SYMBOLS = []
LOOP_SLEEP_TIME = 1

running = True
debug = False
same_tick = {}
stats_orders_shown = 0
positions_total_num = 0
virtual = False
prev_tick_hash = {}


def log(message):
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{date}: {message}")


def normalize_double(value, digits):
    multiplier = 10**digits
    return math.floor(value * multiplier + 0.5) / multiplier


def get_position_type_string(position_type):
    if position_type == mt5.ORDER_TYPE_BUY:
        return "BUY"
    elif position_type == mt5.ORDER_TYPE_SELL:
        return "SELL"
    return "UNKNOWN"


def construct_position(
    position_action,
    type=None,
    symbol=None,
    volume=None,
    price=None,
    sl=None,
    tp=None,
    comment=None,
    ticket=None,
    deviation=None,
):
    position = {"action": position_action}

    if deviation is not None:
        position["deviation"] = deviation
    if type is not None:
        position["type"] = type
    if sl is not None:
        position["sl"] = sl
    if tp is not None:
        position["tp"] = tp
    if price is not None:
        position["price"] = price
    if volume is not None:
        position["volume"] = volume
    if symbol is not None:
        position["symbol"] = symbol
    if comment is not None:
        position["comment"] = comment
    if ticket is not None:
        position["position"] = ticket

    return position


def position_modify(ticket, sl, tp):
    if debug:
        log(f"-> modify position {ticket}: sl=>{sl} tp=>{tp}")

    request = construct_position(
        position_action=mt5.TRADE_ACTION_SLTP, ticket=ticket, sl=sl, tp=tp
    )

    if not virtual:
        res = mt5.order_send(request)
    else:
        res = {"msg": "virtual"}

    if debug:
        rich.inspect(res)
        code, msg = mt5.last_error()
    else:
        code, msg = 0, ""

    if debug:
        log(f"order_send=[{code}: {msg}]")

    return code


def format_position_display(position, tick):
    prf = f"{position.profit:-6.2f}"
    slv = f"{position.sl:,.5f}" if position.sl > 0 else "-       "
    tpv = f"{position.tp:,.5f}" if position.tp > 0 else "-       "
    type_str = get_position_type_string(position.type)
    return prf, slv, tpv, type_str


def ensure_symbol_visible(symbol):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        log(f"Failed to get symbol info for {symbol}")
        return None

    if not symbol_info.visible:
        log(f"{symbol} is not visible, trying to switch on")
        if not mt5.symbol_select(symbol, True):
            log(f"symbol_select({symbol}) failed, skipped")
            return None

    return symbol_info


def calculate_trailing_sl_tp(position, tick, symbol_info):
    global prev_tick_hash, same_tick
    digits = symbol_info.digits
    point = symbol_info.point
    position_type = position.type
    profit = normalize_double(position.profit, 2)
    price_open = normalize_double(position.price_open, digits)
    sl = normalize_double(position.sl, digits)
    tp = normalize_double(position.tp, digits)

    profit_calc = 0.0

    # rich.inspect(symbol)
    # rich.print(f"{2 * point:.6f}")
    hash_tick = hash(
        ":".join([str(tick.ask), str(tick.bid), str(tp), str(sl), str(profit)])
    )
    if prev_tick_hash.get(position.ticket) == hash_tick:
        same_tick[position.ticket] = True
        return -1, -1

    same_tick[position.ticket] = False
    prev_tick_hash[position.ticket] = hash_tick

    if position_type == mt5.ORDER_TYPE_BUY:
        new_profitable_sl = normalize_double(
            tick.ask - FREEZE_SL_POINTS * point,
            digits,
        )

        if profit >= MIN_CURRENT_PROFIT and new_profitable_sl > sl:
            new_sl = normalize_double(
                (tick.ask - TRAIL_PROFIT_STEP * point),
                digits,
            )
            profit_calc = normalize_double(
                position.volume * (tick.ask - price_open) / point, digits
            )
            log(f" -> freezing {profit_calc:5.2f} new_sl={new_sl} sl={sl}")
        else:
            new_sl = normalize_double(tick.ask - TRAIL_STEP * point, digits)

        new_tp = normalize_double(tick.ask + TRAIL_STEP * point, digits)
    else:
        new_profitable_sl = normalize_double(
            tick.bid - FREEZE_SL_POINTS * point, digits
        )
        if profit >= MIN_CURRENT_PROFIT and new_profitable_sl < sl:
            new_sl = normalize_double((tick.bid + TRAIL_PROFIT_STEP * point), digits)
            profit_calc = normalize_double(
                (price_open - tick.bid) * position.volume / point, digits
            )
            log(f" -> freezing {profit_calc:5.2f} new_sl={new_sl} sl={sl}")
        else:
            new_sl = normalize_double(tick.bid + TRAIL_STEP * point, digits)

        new_tp = normalize_double(tick.bid - TRAIL_STEP * point, digits)

    new_sl = normalize_double(new_sl, digits)
    return new_sl, new_tp


def modify_position_if_better(position, new_sl, new_tp):
    ticket = position.ticket
    sl = position.sl
    tp = position.tp
    position_type = position.type
    type_str = get_position_type_string(position_type)

    should_modify_tp = (
        (new_tp > tp or position.tp == 0)
        if position_type == mt5.ORDER_TYPE_BUY
        else (new_tp < tp or position.tp == 0)
    )

    should_modify_sl = (
        (position.sl == 0 or new_sl > sl)
        if position_type == mt5.ORDER_TYPE_BUY
        else (position.sl == 0 or new_sl < sl)
    )

    if not should_modify_tp and not should_modify_sl:
        return

    # Use current values for whichever side shouldn't change
    final_sl = new_sl if should_modify_sl else sl
    final_tp = new_tp if should_modify_tp else tp

    err = position_modify(ticket, final_sl, final_tp)
    if not err:
        if should_modify_sl:
            log(f" -> Modify SL[{type_str}] {sl:.5f} -> {new_sl:.5f}")
        if should_modify_tp:
            log(f" -> Modify TP[{type_str}] {tp:.5f} -> {new_tp:.5f}")
    else:
        log(f" -> Failed to modify {type_str} {ticket}: {mt5.last_error()}")


def process_single_position(position):
    symbol = position.symbol

    if symbol in SKIP_SYMBOLS:
        return

    symbol_info = ensure_symbol_visible(symbol)
    if symbol_info is None:
        return

    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        log(f"Failed to get tick data for {symbol}")
        return

    prf, slv, tpv, type_str = format_position_display(position, tick)

    new_sl, new_tp = calculate_trailing_sl_tp(position, tick, symbol_info)
    if same_tick.get(position.ticket, False) is True:
        return

    log(
        f"{symbol:6s} {type_str:4s} {position.ticket:09d} "
        f"pc={position.price_current:-5.5f} vl={position.volume:3.2f} "
        f"op={position.price_open:4.5f} sl={slv:8s} tp={tpv:8s} "
        f"bid={tick.bid:5.5f} ask={tick.ask:5.5f} {prf:6s}"
    )

    if new_sl != -1:
        modify_position_if_better(position, new_sl, new_tp)


def apply_trailing_tp():
    global positions_total_num
    total_positions = mt5.positions_total()
    if total_positions == 0 or total_positions is None:
        log("No open positions found")
        return

    positions = mt5.positions_get()
    if positions is None:
        log(f"No positions retrieved from {total_positions} total")
        return

    # log(f"---[ positions: {total_positions} ]{'-' * 60}")
    positions_total_num = total_positions

    for position in positions:
        process_single_position(position)


def initialize_mt5():
    if not mt5.initialize():
        log("Failed to initialize MetaTrader 5")
        return False

    log(f"Connected -> MetaTrader {mt5.__version__}")

    info = mt5.account_info()
    if info is None:
        log("Failed to get account info")
        return False
    if debug:
        rich.inspect(info)

    terminal = mt5.terminal_info()
    if terminal is None:
        log("Failed to get terminal info")
        return False
    if debug:
        rich.inspect(terminal)

    return True


def shutdown_mt5():
    mt5.shutdown()
    log("Terminal disconnected")


if __name__ == "__main__":
    log("📉 positions_trailing_tp_mt5.py started 📈")

    if not initialize_mt5():
        sys.exit(1)

    try:
        while running:
            apply_trailing_tp()

            if stats_orders_shown < time.time() - 45:
                log(f"---[ orders: {positions_total_num} ]{'-' * 60}")
                stats_orders_shown = time.time()

            time.sleep(LOOP_SLEEP_TIME)
    except KeyboardInterrupt:
        log("Interrupted by user")
    except Exception:
        rich.traceback.print_exc()
    finally:
        shutdown_mt5()
