#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python 3.14 version of MQL5 script: Print current positions and apply trailing TP
"""

import math

import MetaTrader5 as mt5

# Simulated input parameter
TRAIL_STEP = 10.0  # Trail step in points


class Trade:
    """Simulated trade class similar to MQL5 CTrade"""

    def PositionModify(self, ticket, sl, tp):
        """Modify position SL and TP"""
        print(f"Modified position {ticket}: SL={sl:.5f}, TP={tp:.5f}")


# Simulated market data and position data structures
def SymbolInfoDouble(symbol, info_type):
    """Simulated SymbolInfoDouble function"""
    # In real implementation, this would fetch live market data
    if info_type == "SYMBOL_BID":
        return 1.25000  # Example bid price
    elif info_type == "SYMBOL_ASK":
        return 1.25050  # Example ask price
    return 0.0


def SymbolInfoInteger(symbol, info_type):
    """Simulated SymbolInfoInteger function"""
    if info_type == "SYMBOL_DIGITS":
        return 5  # Example decimal places
    return 0


def PositionsTotal():
    """Return number of open positions"""
    # Simulated data - in real implementation this would connect to trading platform
    return 2


def PositionGetTicket(index):
    """Get ticket of position by index"""
    # Simulated tickets
    tickets = [123456, 789012]
    return tickets[index] if index < len(tickets) else 0


def PositionSelectByTicket(ticket):
    """Select position by ticket"""
    # Simulated selection - always successful in this example
    return True


def PositionGetString(param):
    """Get string parameter of selected position"""
    # Simulated data
    return "EURUSD"


def PositionGetInteger(param):
    """Get integer parameter of selected position"""
    positions_data = {
        123456: {"POSITION_TYPE": 0},  # BUY
        789012: {"POSITION_TYPE": 1},  # SELL
    }

    ticket = PositionGetTicket(0)  # Simplified for example
    if param == "POSITION_TYPE":
        return positions_data.get(ticket, {}).get("POSITION_TYPE", 0)
    return 0


def PositionGetDouble(param):
    """Get double parameter of selected position"""
    # Simulated position data
    positions_data = {
        123456: {
            "POSITION_VOLUME": 1.0,
            "POSITION_PRICE_OPEN": 1.24000,
            "POSITION_SL": 1.23500,
            "POSITION_TP": 1.26000,
            "POSITION_PROFIT": 100.0,
        },
        789012: {
            "POSITION_VOLUME": 0.5,
            "POSITION_PRICE_OPEN": 1.26000,
            "POSITION_SL": 1.26500,
            "POSITION_TP": 1.25000,
            "POSITION_PROFIT": -50.0,
        },
    }

    ticket = PositionGetTicket(0)  # Simplified for example
    return positions_data.get(ticket, {}).get(param, 0.0)


def Print(*args):
    """Simulated Print function"""
    print(*args)


def PrintFormat(format_str, *args):
    """Simulated PrintFormat function"""
    print(format_str % args)


def NormalizeDouble(value, digits):
    """Normalize double to specified decimal places"""
    multiplier = 10**digits
    return math.floor(value * multiplier + 0.5) / multiplier


def OnStart():
    """Main function equivalent to MQL5 OnStart"""
    trade = Trade()

    Print("--- Current Positions Detail ---")
    total = PositionsTotal()

    for i in range(total):
        ticket = PositionGetTicket(i)
        if not PositionSelectByTicket(ticket):
            continue

        symbol = PositionGetString("POSITION_SYMBOL")
        position_type = PositionGetInteger("POSITION_TYPE")
        volume = PositionGetDouble("POSITION_VOLUME")
        price = PositionGetDouble("POSITION_PRICE_OPEN")
        sl = PositionGetDouble("POSITION_SL")
        tp = PositionGetDouble("POSITION_TP")
        profit = PositionGetDouble("POSITION_PROFIT")

        # Convert position type to string
        if position_type == 0:
            type_str = "BUY"
        elif position_type == 1:
            type_str = "SELL"
        else:
            type_str = "UNKNOWN"

        PrintFormat(
            "Ticket:%d Symbol:%s Type:%s Volume:%.2f OpenPrice:%.5f SL:%.5f TP:%.5f Profit:%.2f",
            ticket,
            symbol,
            type_str,
            volume,
            price,
            sl,
            tp,
            profit,
        )

        # Trailing take-profit logic
        if position_type == 0 and tp > 0:  # BUY position
            new_tp = NormalizeDouble(
                SymbolInfoDouble(symbol, "SYMBOL_BID")
                + TRAIL_STEP * (10 ** (-SymbolInfoInteger(symbol, "SYMBOL_DIGITS"))),
                SymbolInfoInteger(symbol, "SYMBOL_DIGITS"),
            )
            if new_tp > tp:
                trade.PositionModify(ticket, sl, new_tp)
        elif position_type == 1 and tp > 0:  # SELL position
            new_tp = NormalizeDouble(
                SymbolInfoDouble(symbol, "SYMBOL_ASK")
                - TRAIL_STEP * (10 ** (-SymbolInfoInteger(symbol, "SYMBOL_DIGITS"))),
                SymbolInfoInteger(symbol, "SYMBOL_DIGITS"),
            )
            if new_tp < tp:
                trade.PositionModify(ticket, sl, new_tp)

    Print("--- End of Positions ---")


# Execute the script
if __name__ == "__main__":
    print("MetaTrader5 package author: ", mt5.__author__)
    print("MetaTrader5 package version: ", mt5.__version__)

    if not mt5.initialize(
        login=108307911, server="MetaQuotes-Demo", password="K-6oLpRs"
    ):
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    # display data on connection status, server name and trading account
    print(mt5.terminal_info())
    # display data on MetaTrader 5 version
    print(mt5.version())
    OnStart()
    #
    # mt5.shutdown()
