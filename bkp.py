"""

Python 3.14 version of MQL5 script: Print current positions and apply trailing TP
Using real MetaTrader5 Python API
"""

import datetime
import math
import sys
import time

import MetaTrader5 as mt5
import rich

# Input parameter for trailing step
TRAIL_STEP = 15.0  # Trail step in points

running = True


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
    if position_type == mt5.POSITION_TYPE_BUY:
        return "BUY"
    elif position_type == mt5.POSITION_TYPE_SELL:
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
        log(
            "------------------------------------------------------------------------------"
        )

        # Get total number of positions
        total_positions = mt5.positions_total()
        if total_positions == 0:
            log("📭 No open positions found")
            return

        # Get all positions
        positions = mt5.positions_get()
        if positions is None:
            log("❌ No positions retrieved")
            return

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
            prf = f"{profit:,.2f}" if profit > 0 else f"-{profit:,.2f}"
            slv = f"{sl:,.5f}" if sl > 0 else f"-       "
            tpv = f"{tp:,.5f}" if tp > 0 else f"-       "

            # Print position details
            log(
                f"🎫 {ticket:09d} {symbol:5s} {type_str:4s} vl:{volume:3.2f} "
                f"op@{price_open:4.5f} sl@{slv:8s} tp@{tpv:8s} {prf:6s}"
            )

            # Apply trailing take-profit logic
            if tp > 0:  # Only if TP is set
                # Get symbol information for precision
                symbol_info = mt5.symbol_info(symbol)
                if symbol_info is None:
                    log(f"❌ Failed to get symbol info for {symbol}")
                    continue

                digits = symbol_info.digits
                point = symbol_info.point

                if position_type == mt5.POSITION_TYPE_BUY:  # BUY position
                    # Get current market data
                    tick = mt5.symbol_info_tick(symbol)
                    if tick is None:
                        log(f"❌ Failed to get tick data for {symbol}")
                        continue

                    # Calculate new TP
                    new_tp = normalize_double(tick.bid + TRAIL_STEP * point, digits)
                    if new_tp > tp:
                        # Modify position
                        result = mt5.position_modify(ticket, sl, new_tp)
                        if result:
                            log(
                                f"✅ Modified BUY position {ticket}: TP updated from {tp:.5f} to {new_tp:.5f}"
                            )
                        else:
                            log(
                                f"❌ Failed to modify BUY position {ticket}: {mt5.last_error()}"
                            )

                elif position_type == mt5.POSITION_TYPE_SELL:  # SELL position
                    # Get current market data
                    tick = mt5.symbol_info_tick(symbol)
                    if tick is None:
                        log(f"❌ Failed to get tick data for {symbol}")
                        continue

                    # Calculate new TP
                    new_tp = normalize_double(tick.ask - TRAIL_STEP * point, digits)
                    if new_tp < tp:
                        # Modify position
                        result = mt5.position_modify(ticket, sl, new_tp)
                        if result:
                            log(
                                f"✅ Modified SELL position {ticket}: TP updated from {tp:.5f} to {new_tp:.5f}"
                            )
                        else:
                            log(
                                f"❌ Failed to modify SELL position {ticket}: {mt5.last_error()}"
                            )

    except Exception as e:
        log(f"💥 Error occurred: {e}")
        dump_backtrace(e)
        # finally:
        # Shutdown connection
        # shutdown_mt5()
        #


def dump_backtrace(e):
    tb = sys.exc_info()
    rich.print(e.with_traceback(tb))


# Execute the script
if __name__ == "__main__":
    log(f"📈  positions_trailing_tp_mt5.py started 📉")

    if not initialize_mt5():
        exit()

    while running:
        apply_trailing_tp()
        time.sleep(3)
