# MetaTrader5 Python API Reference

_Generated automatically – see `extract_mt5_api.py` for details._

## Table of Contents

- [initialize](#initialize)
- [shutdown](#shutdown)
- [version](#version)
- [last_error](#last-error)
- [account_info](#account-info)
- [terminal_info](#terminal-info)
- [symbols_total](#symbols-total)
- [symbols_get](#symbols-get)
- [symbol_info](#symbol-info)
- [symbol_info_tick](#symbol-info-tick)
- [symbol_select](#symbol-select)
- [market_book_add](#market-book-add)
- [market_book_get](#market-book-get)
- [market_book_release](#market-book-release)
- [copy_rates_from](#copy-rates-from)
- [copy_rates_from_pos](#copy-rates-from-pos)
- [copy_rates_range](#copy-rates-range)
- [copy_ticks_from](#copy-ticks-from)
- [copy_ticks_range](#copy-ticks-range)
- [orders_total](#orders-total)
- [orders_get](#orders-get)
- [order_calc_margin](#order-calc-margin)
- [order_calc_profit](#order-calc-profit)
- [order_check](#order-check)
- [order_send](#order-send)
- [positions_total](#positions-total)
- [positions_get](#positions-get)
- [history_orders_total](#history-orders-total)
- [history_orders_get](#history-orders-get)
- [history_deals_total](#history-deals-total)
- [history_deals_get](#history-deals-get)

## `initialize`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py)

### Parameters
*None*  

---

## `shutdown`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py)

### Parameters
*None*  

---

## `version`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5version_py)

### Parameters
*None*  

---

## `last_error`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py)

### Parameters
*None*  

---

## `account_info`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py)

### Parameters
*None*  

---

## `terminal_info`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py)

### Parameters
*None*  

---

## `symbols_total`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py)

### Parameters
*None*  

---

## `symbols_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py)

### Parameters
*None*  

---

## `symbol_info`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py)

### Parameters
*None*  

---

## `symbol_info_tick`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py)

### Parameters
*None*  

---

## `symbol_select`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py)

### Parameters
*None*  

---

## `market_book_add`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py)

### Parameters
*None*  

---

## `market_book_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py)

### Parameters
*None*  

---

## `market_book_release`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py)

### Parameters
*None*  

---

## `copy_rates_from`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py)

### Parameters
| Name | Description |
|---|---|
| symbol | [in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | [in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter. |
| date_from | [in]  Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| count | [in]  Number of bars to receive. Required unnamed parameter. |

---

## `copy_rates_from_pos`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py)

### Parameters
| Name | Description |
|---|---|
| symbol | [in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | [in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter. |
| start_pos | [in]  Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter. |
| count | [in]  Number of bars to receive. Required unnamed parameter. |

---

## `copy_rates_range`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py)

### Parameters
| Name | Description |
|---|---|
| symbol | [in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | [in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter. |
| date_from | [in]  Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter. |
| date_to | [in]  Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter. |

---

## `copy_ticks_from`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py)

### Parameters
| Name | Description |
|---|---|
| symbol | [in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| from | [in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| count | [in]  Number of ticks to receive. Required unnamed parameter. |
| flags | [in]  A flag to define the type of the requested ticks.COPY_TICKS_INFO– ticks with Bid and/or Ask changes,COPY_TICKS_TRADE– ticks with changes in Last and Volume,COPY_TICKS_ALL– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter. |

---

## `copy_ticks_range`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py)

### Parameters
| Name | Description |
|---|---|
| symbol | [in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| date_from | [in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| date_to | [in]  Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| flags | [in]  A flag to define the type of the requested ticks.COPY_TICKS_INFO– ticks with Bid and/or Ask changes,COPY_TICKS_TRADE– ticks with changes in Last and Volume,COPY_TICKS_ALL– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter. |

---

## `orders_total`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py)

### Parameters
*None*  

---

## `orders_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py)

### Parameters
| Name | Description |
|---|---|
| symbol="SYMBOL" | [in]  Symbol name. Optional named parameter. If a symbol is specified, theticketparameter is ignored. |
| group="GROUP" | [in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only active orders meeting a specified criteria for a symbol name. |
| ticket=TICKET | [in]  Order ticket (ORDER_TICKET). Optional named parameter. |

---

## `order_calc_margin`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py)

### Parameters
| Name | Description |
|---|---|
| action | [in]  Order type taking values from theORDER_TYPEenumeration. Required unnamed parameter. |
| symbol | [in]  Financial instrument name. Required unnamed parameter. |
| volume | [in]  Trading operation volume. Required unnamed parameter. |
| price | [in]  Open price. Required unnamed parameter. |

---

## `order_calc_profit`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py)

### Parameters
| Name | Description |
|---|---|
| action | [in]  Order type may take one of the twoORDER_TYPEenumeration values: ORDER_TYPE_BUY or ORDER_TYPE_SELL. Required unnamed parameter. |
| symbol | [in]  Financial instrument name. Required unnamed parameter. |
| volume | [in]  Trading operation volume. Required unnamed parameter. |
| price_open | [in]  Open price. Required unnamed parameter. |
| price_close | [in]  Close price. Required unnamed parameter. |

---

## `order_check`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py)

### Parameters
| Name | Description |
|---|---|
| request | [in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below. |

---

## `order_send`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py)

### Parameters
| Name | Description |
|---|---|
| request | [in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below. |

---

## `positions_total`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py)

### Parameters
*None*  

---

## `positions_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py)

### Parameters
*None*  

---

## `history_orders_total`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py)

### Parameters
| Name | Description |
|---|---|
| date_from | [in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| date_to | [in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |

---

## `history_orders_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py)

### Parameters
| Name | Description |
|---|---|
| date_from | [in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first. |
| date_to | [in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second. |
| group="GROUP" | [in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name. |
| ticket=TICKET | [in]  Order ticket that should be received. Optional parameter. If not specified, the filter is not applied. |
| position=POSITION | [in]  Ticket of a position (stored inORDER_POSITION_ID) all orders should be received for. Optional parameter. If not specified, the filter is not applied. |

---

## `history_deals_total`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py)

### Parameters
| Name | Description |
|---|---|
| date_from | [in]  Date the deals are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| date_to | [in]  Date, up to which the deals are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |

---

## `history_deals_get`
[Documentation page](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py)

### Parameters
| Name | Description |
|---|---|
| date_from | [in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first. |
| date_to | [in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second. |
| group="GROUP" | [in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name. |
| ticket=TICKET | [in]  Ticket of an order (stored inDEAL_ORDER) all deals should be received for. Optional parameter. If not specified, the filter is not applied. |
| position=POSITION | [in]  Ticket of a position (stored inDEAL_POSITION_ID) all deals should be received for. Optional parameter. If not specified, the filter is not applied. |

---

