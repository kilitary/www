# MetaTrader5 Python API Reference

_Generated automatically – see `extract_mt5_api.py` for details._

## Table of Contents

- [initialize](#initialize)
- [shutdown](#shutdown)
- [version](#version)
- [last_error](#last_error)
- [account_info](#account_info)
- [terminal_info](#terminal_info)
- [symbols_total](#symbols_total)
- [symbols_get](#symbols_get)
- [symbol_info](#symbol_info)
- [symbol_info_tick](#symbol_info_tick)
- [symbol_select](#symbol_select)
- [market_book_add](#market_book_add)
- [market_book_get](#market_book_get)
- [market_book_release](#market_book_release)
- [copy_rates_from](#copy_rates_from)
- [copy_rates_from_pos](#copy_rates_from_pos)
- [copy_rates_range](#copy_rates_range)
- [copy_ticks_from](#copy_ticks_from)
- [copy_ticks_range](#copy_ticks_range)
- [orders_total](#orders_total)
- [orders_get](#orders_get)
- [order_calc_margin](#order_calc_margin)
- [order_calc_profit](#order_calc_profit)
- [order_check](#order_check)
- [order_send](#order_send)
- [positions_total](#positions_total)
- [positions_get](#positions_get)
- [history_orders_total](#history_orders_total)
- [history_orders_get](#history_orders_get)
- [history_deals_total](#history_deals_total)
- [history_deals_get](#history_deals_get)

## `initialize`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)

### Signatures
- `initialize()`
- `initialize(path)`
- `initialize(path, login=LOGIN, password="PASSWORD", server="SERVER", timeout=TIMEOUT, portable=False)`

### Parameters
| Name | Description |
|---|
| path | [in] Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. It is indicated first without a parameter name. If the path is not specified, the module attempts to find the executable file on its own. |
| login=LOGIN | [in] Trading account number. Optional named parameter. If not specified, the last trading account is used. |
| password="PASSWORD" | [in] Trading account password. Optional named parameter. If the password is not set, the password for a specified trading account saved in the terminal database is applied automatically. |
| server="SERVER" | [in] Trade server name. Optional named parameter. If the server is not set, the server for a specified trading account saved in the terminal database is applied automatically. |
| timeout=TIMEOUT | [in] Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied. |
| portable=False | [in] Flag of the terminal launch in portable mode. Optional named parameter. If not specified, the value of False is used. |

### Returns
**Type:** `bool`

Returns `True` in case of successful connection to the MetaTrader 5 terminal, otherwise `False`. Note: If required, the MetaTrader 5 terminal is launched to establish connection when executing the initialize() call.

### Example
```python
import MetaTrader5 as mt5

# establish MetaTrader 5 connection to a specified trading account
if not mt5.initialize(login=25115284, server="MetaQuotes-Demo", password="4zatlbqx"):
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# display data on connection status, server name and trading account
print(mt5.terminal_info())

# display data on MetaTrader 5 version
print(mt5.version())

---

## `shutdown`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)

### Signatures
- `shutdown()`

### Parameters
*None*

### Returns
**Type:** `None`

Closes the previously established connection to the MetaTrader 5 terminal.

### Example
```python
import MetaTrader5 as mt5

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# display data on connection status, server name and trading account
print(mt5.terminal_info())

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

---

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

--- 
