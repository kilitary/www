# MetaTrader 5 Python API Reference

This document provides detailed signatures, parameter descriptions, return types, and usage examples for each function in the MetaTrader5 Python package.

## Installation
```bash
pip install MetaTrader5
```

---

## Functions

### 1. `initialize`
```python
initialize([path], [server="SERVER"], [login=LOGIN], [password="PASSWORD"]) -> bool
```
- **Description**: Establish a connection to the MetaTrader 5 terminal.
- **Parameters**:
  - `path` *(optional)*: Path to the terminal executable. If omitted, the default installed terminal is used.
  - `server` *(optional, default="SERVER")*: Server name to connect to.
  - `login` *(optional)*: Account login number.
  - `password` *(optional, default="PASSWORD")*: Account password.
- **Returns**: `True` on successful connection, `False` otherwise.
- **Example**:
```python
import MetaTrader5 as mt5
if not mt5.initialize():
    print("Failed to connect")
    mt5.shutdown()
```
---

### 2. `login`
```python
login(login, [server="SERVER"], [password="PASSWORD"]) -> bool
```
- **Description**: Log in to a specific trading account.
- **Parameters**:
  - `login` *(int)*: Account login number.
  - `server` *(optional, default="SERVER")*: Server name.
  - `password` *(optional, default="PASSWORD")*: Account password.
- **Returns**: `True` if login succeeded, `False` otherwise.
- **Example**:
```python
mt5.login(12345678, server="Demo", password="myPass")
```
---

### 3. `shutdown`
```python
shutdown() -> bool
```
- **Description**: Disconnect from the MetaTrader 5 terminal.
- **Parameters**: None.
- **Returns**: `True` on success.
- **Example**:
```python
mt5.shutdown()
```
---

### 4. `version`
```python
version() -> str
```
- **Description**: Get the MetaTrader 5 terminal version string.
- **Parameters**: None.
- **Returns**: Version string, e.g. `"5.0.0"`.
- **Example**:
```python
print(mt5.version())
```
---

### 5. `last_error`
```python
last_error() -> int
```
- **Description**: Return the last error code and description.
- **Parameters**: None.
- **Returns**: Integer error code (0 means no error).
- **Example**:
```python
err = mt5.last_error()
print("Last error:", err)
```
---

### 6. `account_info`
```python
account_info() -> dict
```
- **Description**: Return information about the currently connected account.
- **Parameters**: None.
- **Returns**: Dictionary with fields such as `balance`, `equity`, `margin`, `leverage`, etc.
- **Example**:
```python
info = mt5.account_info()
print(info.balance, info.equity)
```
---

### 7. `terminal_info`
```python
terminal_info() -> dict
```
- **Description**: Get parameters of the MetaTrader 5 terminal.
- **Parameters**: None.
- **Returns**: Dictionary containing terminal version, build, path, etc.
- **Example**:
```python
print(mt5.terminal_info())
```
---

### 8. `symbols_total`
```python
symbols_total() -> int
```
- **Description**: Return the total number of symbols available in the terminal.
- **Parameters**: None.
- **Returns**: Integer count.
- **Example**:
```python
print("Symbols count:", mt5.symbols_total())
```
---

### 9. `symbols_get`
```python
symbols_get([group="GROUP"]) -> list[dict]
```
- **Description**: Retrieve all symbols, optionally filtered by group.
- **Parameters**:
  - `group` *(optional)*: Symbol group name (e.g., "forex").
- **Returns**: List of dictionaries, each describing a symbol.
- **Example**:
```python
symbols = mt5.symbols_get()
print(symbols[0])
```
---

### 10. `symbol_info`
```python
symbol_info(symbol) -> dict
```
- **Description**: Get full information for a specific symbol.
- **Parameters**:
  - `symbol` *(str)*: Symbol name, e.g., "EURUSD".
- **Returns**: Dictionary with details such as `point`, `trade_tick_size`, `trade_tick_value`, etc.
- **Example**:
```python
info = mt5.symbol_info("EURUSD")
print(info.point)
```
---

### 11. `symbol_info_tick`
```python
symbol_info_tick(symbol) -> dict
```
- **Description**: Retrieve the latest tick (bid/ask) for a symbol.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
- **Returns**: Dictionary with `bid`, `ask`, `last`, `time`.
- **Example**:
```python
tick = mt5.symbol_info_tick("EURUSD")
print(tick.bid, tick.ask)
```
---

### 12. `symbol_select`
```python
symbol_select(symbol, [enable]) -> bool
```
- **Description**: Add or remove a symbol from the MarketWatch window.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
  - `enable` *(optional, default=True)*: `True` to add, `False` to remove.
- **Returns**: `True` on success.
- **Example**:
```python
mt5.symbol_select("GBPUSD", True)   # add
mt5.symbol_select("GBPUSD", False)  # remove
```
---

### 13. `market_book_add`
```python
market_book_add(symbol) -> bool
```
- **Description**: Subscribe to Market Depth (order book) updates for a symbol.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
- **Returns**: `True` if subscription succeeded.
- **Example**:
```python
mt5.market_book_add("EURUSD")
```
---

### 14. `market_book_get`
```python
market_book_get(symbol) -> list[dict]
```
- **Description**: Retrieve the current Market Depth data for a symbol.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
- **Returns**: List of depth entries (price, volume, type).
- **Example**:
```python
book = mt5.market_book_get("EURUSD")
print(book[:5])
```
---

### 15. `market_book_release`
```python
market_book_release(symbol) -> bool
```
- **Description**: Cancel the Market Depth subscription for a symbol.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
- **Returns**: `True` on success.
- **Example**:
```python
mt5.market_book_release("EURUSD")
```
---

### 16. `copy_rates_from`
```python
copy_rates_from(symbol, timeframe, date_from, count) -> list[dict]
```
- **Description**: Get historical bar data starting from a specific date.
- **Parameters**:
  - `symbol` *(str)*: Symbol name.
  - `timeframe` *(int)*: One of `mt5.TIMEFRAME_M1`, `mt5.TIMEFRAME_H1`, etc.
  - `date_from` *(datetime)*: Starting date/time.
  - `count` *(int)*: Number of bars to retrieve.
- **Returns**: List of bar dictionaries (`time`, `open`, `high`, `low`, `close`, `tick_volume`, `spread`, `real_volume`).
- **Example**:
```python
from datetime import datetime
bars = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2022,1,1), 500)
print(bars[0])
```
---

### 17. `copy_rates_from_pos`
```python
copy_rates_from_pos(symbol, timeframe, start_pos, count) -> list[dict]
```
- **Description**: Get historical bars starting from a position index.
- **Parameters**:
  - `symbol` *(str)*
  - `timeframe` *(int)*
  - `start_pos` *(int)*: Zero‑based index (0 = most recent bar).
  - `count` *(int)*
- **Returns**: List of bar dictionaries.
- **Example**:
```python
bars = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_H1, 0, 100)
```
---

### 18. `copy_rates_range`
```python
copy_rates_range(symbol, timeframe, date_from, date_to) -> list[dict]
```
- **Description**: Retrieve bars for a date interval.
- **Parameters**:
  - `symbol` *(str)*
  - `timeframe` *(int)*
  - `date_from` *(datetime)*
  - `date_to` *(datetime)*
- **Returns**: List of bar dictionaries.
- **Example**:
```python
bars = mt5.copy_rates_range("EURUSD", mt5.TIMEFRAME_D1, datetime(2021,1,1), datetime(2021,12,31))
```
---

### 19. `copy_ticks_from`
```python
copy_ticks_from(symbol, date_from, count, flags) -> list[dict]
```
- **Description**: Get tick data starting from a date.
- **Parameters**:
  - `symbol` *(str)*
  - `date_from` *(datetime)*
  - `count` *(int)*
  - `flags` *(int)*: Bitmask, e.g., `mt5.COPY_TICKS_ALL`.
- **Returns**: List of tick dictionaries (`time`, `bid`, `ask`, `last`, `volume`, `flags`).
- **Example**:
```python
ticks = mt5.copy_ticks_from("EURUSD", datetime(2022,5,1), 1000, mt5.COPY_TICKS_ALL)
```
---

### 20. `copy_ticks_range`
```python
copy_ticks_range(symbol, date_from, date_to, flags) -> list[dict]
```
- **Description**: Retrieve ticks for a date interval.
- **Parameters**:
  - `symbol` *(str)*
  - `date_from` *(datetime)*
  - `date_to` *(datetime)*
  - `flags` *(int)*
- **Returns**: List of tick dictionaries.
- **Example**:
```python
ticks = mt5.copy_ticks_range("EURUSD", datetime(2022,5,1), datetime(2022,5,2), mt5.COPY_TICKS_ALL)
```
---

### 21. `orders_total`
```python
orders_total() -> int
```
- **Description**: Return the number of active orders.
- **Parameters**: None.
- **Returns**: Integer count.
- **Example**:
```python
print(mt5.orders_total())
```
---

### 22. `orders_get`
```python
orders_get([symbol="SYMBOL"], [ticket=TICKET], [group="GROUP"]) -> list[dict]
```
- **Description**: Retrieve active orders, optionally filtered.
- **Parameters**:
  - `symbol` *(optional)*: Filter by symbol.
  - `ticket` *(optional)*: Specific order ticket.
  - `group` *(optional)*: Order group.
- **Returns**: List of order dictionaries.
- **Example**:
```python
orders = mt5.orders_get(symbol="EURUSD")
print(orders)
```
---

### 23. `order_calc_margin`
```python
order_calc_margin(action, symbol, volume, price) -> float
```
- **Description**: Calculate required margin for a trade request.
- **Parameters**:
  - `action` *(int)*: Order type (`mt5.ORDER_TYPE_BUY`, `mt5.ORDER_TYPE_SELL`, etc.).
  - `symbol` *(str)*
  - `volume` *(float)*: Lots.
  - `price` *(float)*: Execution price.
- **Returns**: Margin in account currency.
- **Example**:
```python
margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, "EURUSD", 0.1, 1.1200)
print(margin)
```
---

### 24. `order_calc_profit`
```python
order_calc_profit(action, symbol, volume, price_open, price_close) -> float
```
- **Description**: Compute profit for a hypothetical trade.
- **Parameters**:
  - `action` *(int)*
  - `symbol` *(str)*
  - `volume` *(float)*
  - `price_open` *(float)*
  - `price_close` *(float)*
- **Returns**: Profit in account currency.
- **Example**:
```python
profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, "EURUSD", 0.1, 1.1200, 1.1250)
print(profit)
```
---

### 25. `order_check`
```python
order_check(request) -> bool
```
- **Description**: Validate a trade request (margin, price, etc.).
- **Parameters**:
  - `request` *(dict)*: Trade request dictionary (see MT5 docs for fields).
- **Returns**: `True` if request is valid.
- **Example**:
```python
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": "EURUSD",
    "volume": 0.1,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick("EURUSD").ask,
    "deviation": 10,
    "magic": 123456,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
if mt5.order_check(request):
    print("Request OK")
```
---

### 26. `order_send`
```python
order_send(request) -> int  # ticket of the placed order
```
- **Description**: Send a trade request to the server.
- **Parameters**:
  - `request` *(dict)*: Same structure as for `order_check`.
- **Returns**: Ticket number of the placed order (or 0 on failure).
- **Example**:
```python
result = mt5.order_send(request)
print("Order ticket:", result)
```
---

### 27. `positions_total`
```python
positions_total() -> int
```
- **Description**: Number of open positions.
- **Parameters**: None.
- **Returns**: Integer count.
- **Example**:
```python
print(mt5.positions_total())
```
---

### 28. `positions_get`
```python
positions_get([symbol="SYMBOL"], [ticket=TICKET], [group="GROUP"]) -> list[dict]
```
- **Description**: Retrieve open positions, optionally filtered.
- **Parameters**:
  - `symbol` *(optional)*
  - `ticket` *(optional)*
  - `group` *(optional)*
- **Returns**: List of position dictionaries.
- **Example**:
```python
pos = mt5.positions_get(symbol="EURUSD")
print(pos)
```
---

### 29. `history_orders_total`
```python
history_orders_total(date_from, date_to) -> int
```
- **Description**: Number of orders in a historical interval.
- **Parameters**:
  - `date_from` *(datetime)*
  - `date_to` *(datetime)*
- **Returns**: Integer count.
- **Example**:
```python
cnt = mt5.history_orders_total(datetime(2021,1,1), datetime(2021,12,31))
print(cnt)
```
---

### 30. `history_orders_get`
```python
history_orders_get([date_from, date_to, [group="GROUP"]], [position=POSITION], [ticket=TICKET]) -> list[dict]
```
- **Description**: Retrieve historical orders with optional filters.
- **Parameters**:
  - `date_from`, `date_to` *(optional datetime)*
  - `group` *(optional)*
  - `position` *(optional int)*: Position ID.
  - `ticket` *(optional int)*: Order ticket.
- **Returns**: List of order dictionaries.
- **Example**:
```python
orders = mt5.history_orders_get(date_from=datetime(2021,1,1), date_to=datetime(2021,12,31))
print(orders[:3])
```
---

### 31. `history_deals_total`
```python
history_deals_total(date_from, date_to) -> int
```
- **Description**: Number of deals in a historical interval.
- **Parameters**:
  - `date_from`, `date_to` *(datetime)*
- **Returns**: Integer count.
- **Example**:
```python
cnt = mt5.history_deals_total(datetime(2021,1,1), datetime(2021,12,31))
print(cnt)
```
---

### 32. `history_deals_get`
```python
history_deals_get([date_from, date_to, [group="GROUP"]], [position=POSITION], [ticket=TICKET]) -> list[dict]
```
- **Description**: Retrieve historical deals with optional filters.
- **Parameters**:
  - Same as `history_orders_get`.
- **Returns**: List of deal dictionaries.
- **Example**:
```python
deals = mt5.history_deals_get(date_from=datetime(2021,1,1), date_to=datetime(2021,12,31))
print(deals[:3])
```
---

## Quick Start Example
```python
import MetaTrader5 as mt5
from datetime import datetime

if not mt5.initialize():
    raise SystemExit("initialize() failed")

print("Terminal version:", mt5.version())
print("Account balance:", mt5.account_info().balance)

# Get last 5 minute bars for EURUSD
bars = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime.now(), 5)
for b in bars:
    print(b)

mt5.shutdown()
```

*For a complete reference, see the official documentation at https://www.mql5.com/en/docs/python_metatrader5.*