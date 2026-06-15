"""

Python 3.14 version of MQL5 script: Print current positions and apply trailing TP
Using real MetaTrader5 Python API
"""

import math
import sys
import time

import MetaTrader5 as mt5
import rich

# Input parameter for trailing step
TRAIL_STEP = 45.0  # Trail step in points
MIN_PROFIT_POINTS = 15
NUM_TRAIL_PROFITABLE = 45
MIN_CURRENT_PROFIT = 4.0

loop_sleep_time = 1
running = True
debug_modify = False


def position_modify(ticket, sl, tp):
    if debug_modify:
        log(f"-> modify position {ticket}: sl=>{sl} tp=>{tp}")

    request = construct_position(
        position_action=mt5.TRADE_ACTION_SLTP, ticket=ticket, sl=sl, tp=tp
    )
    res = mt5.order_send(request)

    if debug_modify:
        rich.inspect(res)

    err = mt5.last_error()

    if debug_modify:
        log(f"order_send=[{err}]")

    return err


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

    if deviation:
        position["deviation"] = deviation

    if type:
        position["type"] = type

    if sl:
        position["sl"] = sl
    if tp:
        position["tp"] = tp

    if price:
        position["price"] = price
    if volume:
        position["volume"] = volume

    if symbol:
        position["symbol"] = symbol

    if comment is not None:
        position["comment"] = comment

    if ticket is not None:
        position["position"] = ticket

    return position


def initialize_mt5():
    """Initialize connection to MetaTrader 5"""
    if not mt5.initialize():
        log("❌ Failed to initialize MetaTrader 5")
        return False
    log(f"✅ Connect -> MetaTrader {mt5.__version__}")
    info = mt5.account_info()
    if info is None:
        log("❌ Failed to get account info")
        return False
    rich.print(info)
    return True


def shutdown_mt5():
    """Shutdown connection to MetaTrader 5"""
    mt5.shutdown()
    log("🔚 terminal proc disconnect")


def normalize_double(value, digits):
    """Normalize double to specified decimal places"""
    multiplier = 10**digits
    return math.floor(value * multiplier + 0.5) / multiplier


def get_position_type_string(position_type):
    """Convert position type to string"""
    if position_type == mt5.ORDER_TYPE_BUY:
        return "BUY"
    elif position_type == mt5.ORDER_TYPE_SELL:
        return "SELL"
    else:
        return "❓ UNKNOWN"


def log(message):
    """Log a message to the console"""
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"📝 {date}: {message}")


def apply_trailing_tp():
    """Main function to print positions and apply trailing TP"""
    try:
        # Get total number of positions
        total_positions = mt5.positions_total()
        if total_positions == 0 or total_positions is None:
            log("📭 No open positions found")
            return

        # Get all positions
        positions = mt5.positions_get()
        if positions is None:
            log(f"❌ No positions retrieved from {total_positions} total")
            return

        log(
            f"-------------------------[ positions: {total_positions} ]----------------------------------------------"
        )

        # Process each position
        for position in positions:
            ticket = position.ticket
            symbol = position.symbol
            position_type = position.type
            volume = position.volume
            price_open = position.price_open
            sl = position.sl
            tp = position.tp
            profit = position.profit

            # Convert position type to string
            type_str = get_position_type_string(position_type)
            prf = f"{profit:-6.2f}" if profit > 0 else f"{profit:-6.2f}"
            slv = f"{sl:,.5f}" if sl > 0 else "-       "
            tpv = f"{tp:,.5f}" if tp > 0 else "-       "



            # Get symbol information for precision
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                log(f"❌ Failed to get symbol info for {symbol}")
                continue
            else:
                # rich.inspect(symbol_info)
                pass

            if not symbol_info.visible:
                    print(symbol, "is not visible, trying to switch on")
                    if not mt5.symbol_select(symbol,True):
                        print("symbol_select({}}) failed, skipped",symbol)
                        continue

            #rich.inspect(symbol_info)

            digits = symbol_info.digits
            point = symbol_info.point

            tick = mt5.symbol_info_tick(symbol)
            if tick is None:
                log(f"❌ Failed to get tick data for {symbol}")
                continue

            #rich.inspect(position)
            #rich.inspect(symbol)

            #rich.print(f"{point}")

            profit_calc = 0.0

            log(
                f"{symbol:5s} {type_str:4s} {ticket:09d} pc={position.price_current:-5.5f} vl={volume:3.2f} "
                f"op={price_open:4.5f} sl={slv:8s} tp={tpv:8s} {prf:6s}"
            )

            # BUY position
            if position_type == mt5.ORDER_TYPE_BUY:
                new_profitable_sl = normalize_double(tick.ask + NUM_TRAIL_PROFITABLE * 1.2 * point, digits)
                if profit >= MIN_CURRENT_PROFIT and new_profitable_sl > sl:
                    new_sl = normalize_double(position.volume * (tick.ask + (price_open - tick.bid)), digits)
                    profit_calc = float(position.volume * (tick.ask - price_open) / point)
                    log(f" -> freezing {profit_calc:-6.2f} at {new_sl} new_sl={new_sl} sl={sl}")
                else:
                    new_sl = normalize_double(tick.bid - TRAIL_STEP * point, digits)

                new_tp = normalize_double(tick.bid + TRAIL_STEP * point, digits)

            # SELL position
            else:
                new_profitable_sl = normalize_double(position.sl - NUM_TRAIL_PROFITABLE * 1.2 * point, digits)
                if profit >= MIN_CURRENT_PROFIT and new_profitable_sl < sl:
                    new_sl = normalize_double(position.volume * (price_open + tick.ask - tick.bid) , digits)
                    profit_calc = float(position.volume * (price_open - tick.bid) / point)
                    log(f" -> freezing {profit_calc:-6.2f} new_sl={new_sl} sl={sl}")
                else:
                    new_sl = normalize_double(tick.ask + TRAIL_STEP * point, digits)

                new_tp = normalize_double(tick.ask - TRAIL_STEP * point, digits)

            new_sl = normalize_double(new_sl, digits)

            if position_type == mt5.ORDER_TYPE_BUY:  # BUY position
                if new_tp > tp or position.tp == 0:
                    result = position_modify(ticket, new_sl, new_tp)
                    if result:
                        log(
                            f" -> ✅ Modify TP[ {tp:.5f} -> {new_tp:.5f}]"
                        )
                    else:
                        log(
                            f"-> ❌ Failed to modify SELL position {ticket}: {mt5.last_error()}"
                        )
                if position.sl == 0 or new_sl > sl:
                    result = position_modify(ticket, new_sl, new_tp)
                    if result:
                        log(
                            f" -> ✅ Modify SL[ {sl:.5f} -> {new_sl:.5f}]"
                        )
                    else:
                        log(
                            f"-> ❌ Failed to modify SELL position {ticket}: {mt5.last_error()}"
                        )
            else:
                if new_tp < tp or position.tp == 0:
                    result = position_modify(ticket, new_sl, new_tp)
                    if result:
                        log(
                            f" -> ✅ Modify TP[ {tp:.5f} -> {new_tp:.5f}]"
                        )
                    else:
                        log(
                            f"-> ❌ Failed to modify SELL position {ticket}: {mt5.last_error()}"
                        )
                if position.sl == 0 or new_sl < sl:
                    result = position_modify(ticket, new_sl, new_tp)
                    if result:
                        log(
                            f" -> ✅ Modify SL[ {sl:.5f} -> {new_sl:.5f}]"
                        )
                    else:
                        log(
                            f"-> ❌ Failed to modify SELL position {ticket}: {mt5.last_error()}"
                        )

    except Exception as e:
        tb = sys.exc_info()[2]
        log(f"💥 Error occurred: {e}")
        dump_backtrace(tb)

        # finally:
        # Shutdown connection
        shutdown_mt5()


def dump_backtrace(tb):
    rich.print(tb.tb_next.tb_frame)


# Execute the script
if __name__ == "__main__":
    log("📈  positions_trailing_tp_mt5.py started 📉")

    if not initialize_mt5():
        exit()

    while running:
        apply_trailing_tp()

        time.sleep(loop_sleep_time)
