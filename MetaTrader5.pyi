"""Type stubs for the MetaTrader 5 Python package.

MetaTrader 5 Python API provides programmatic access to the MetaTrader 5
trading platform, including trading operations, market data retrieval,
and account/terminal information.
"""
from datetime import datetime
from typing import Any, NamedTuple, Sequence, overload

import numpy as np

__version__: str
"""The version string of the MetaTrader5 package."""

__author__: str
"""The author of the MetaTrader5 package."""

# ─────────────────────────────────────────────────────────────────────
# ORDER_TYPE – Types of trade orders (ENUM_ORDER_TYPE)
# ─────────────────────────────────────────────────────────────────────

ORDER_TYPE_BUY: int
"""Market Buy order."""

ORDER_TYPE_SELL: int
"""Market Sell order."""

ORDER_TYPE_BUY_LIMIT: int
"""Buy Limit pending order."""

ORDER_TYPE_SELL_LIMIT: int
"""Sell Limit pending order."""

ORDER_TYPE_BUY_STOP: int
"""Buy Stop pending order."""

ORDER_TYPE_SELL_STOP: int
"""Sell Stop pending order."""

ORDER_TYPE_BUY_STOP_LIMIT: int
"""Upon reaching the order price, a pending Buy Limit order is placed at the StopLimit price."""

ORDER_TYPE_SELL_STOP_LIMIT: int
"""Upon reaching the order price, a pending Sell Limit order is placed at the StopLimit price."""

ORDER_TYPE_CLOSE_BY: int
"""Order to close a position by an opposite one."""

# ─────────────────────────────────────────────────────────────────────
# ORDER_TIME – Order lifetime (ENUM_ORDER_TYPE_TIME)
# ─────────────────────────────────────────────────────────────────────

ORDER_TIME_GTC: int
"""Good till cancel order."""

ORDER_TIME_DAY: int
"""Good till current trade day order."""

ORDER_TIME_SPECIFIED: int
"""Good till expired order."""

ORDER_TIME_SPECIFIED_DAY: int
"""The order will be effective till 23:59:59 of the specified day. If this time is outside a trading session, the order expires in the nearest trading time."""

# ─────────────────────────────────────────────────────────────────────
# ORDER_FILLING – Order filling policy (ENUM_ORDER_TYPE_FILLING)
# ─────────────────────────────────────────────────────────────────────

ORDER_FILLING_FOK: int
"""Fill or Kill – an order can be executed in the specified volume only. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed."""

ORDER_FILLING_IOC: int
"""Immediate or Cancel – a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled."""

ORDER_FILLING_BOC: int
"""Book or Cancel – the order can only be placed in the Depth of Market and cannot be immediately executed. If the order can be executed immediately when placed, then it is canceled. Only limit and stop limit orders are supported."""

ORDER_FILLING_RETURN: int
"""Return – in case of partial filling, an order with remaining volume is not canceled but processed further. Return orders are not allowed in the Market Execution mode (SYMBOL_TRADE_EXECUTION_MARKET)."""

# ─────────────────────────────────────────────────────────────────────
# TRADE_ACTION – Types of trade operations (ENUM_TRADE_REQUEST_ACTIONS)
# ─────────────────────────────────────────────────────────────────────

TRADE_ACTION_SLTP: int
"""Modify Stop Loss and Take Profit values of an opened position."""

TRADE_ACTION_DEAL: int
"""Place a trade order for an immediate execution with the specified parameters (market order)."""

TRADE_ACTION_PENDING: int
"""Place a trade order for the execution under specified conditions (pending order)."""

TRADE_ACTION_MODIFY: int
"""Modify the parameters of the order placed previously."""

TRADE_ACTION_REMOVE: int
"""Delete the pending order placed previously."""

TRADE_ACTION_CLOSE_BY: int
"""Close a position by an opposite one."""

# ─────────────────────────────────────────────────────────────────────
# ORDER_STATE – Order states (ENUM_ORDER_STATE)
# ─────────────────────────────────────────────────────────────────────

ORDER_STATE_STARTED: int
"""Order checked, but not yet accepted by broker."""

ORDER_STATE_PLACED: int
"""Order accepted."""

ORDER_STATE_CANCELED: int
"""Order canceled by client."""

ORDER_STATE_PARTIAL: int
"""Order partially executed."""

ORDER_STATE_FILLED: int
"""Order fully executed."""

ORDER_STATE_REJECTED: int
"""Order rejected."""

ORDER_STATE_EXPIRED: int
"""Order expired."""

ORDER_STATE_REQUEST_ADD: int
"""Order is being registered (placing to the trading system)."""

ORDER_STATE_REQUEST_MODIFY: int
"""Order is being modified (changing its parameters)."""

ORDER_STATE_REQUEST_CANCEL: int
"""Order is being deleted (deleting from the trading system)."""

# ─────────────────────────────────────────────────────────────────────
# ORDER_REASON – Reason for placing an order (ENUM_ORDER_REASON)
# ─────────────────────────────────────────────────────────────────────

ORDER_REASON_CLIENT: int
"""The order was placed from a desktop terminal."""

ORDER_REASON_MOBILE: int
"""The order was placed from a mobile application."""

ORDER_REASON_WEB: int
"""The order was placed from a web platform."""

ORDER_REASON_EXPERT: int
"""The order was placed from an MQL5 program (Expert Advisor or script)."""

ORDER_REASON_SL: int
"""The order was placed as a result of Stop Loss activation."""

ORDER_REASON_TP: int
"""The order was placed as a result of Take Profit activation."""

ORDER_REASON_SO: int
"""The order was placed as a result of the Stop Out event."""

# ─────────────────────────────────────────────────────────────────────
# TRADE_RETCODE – Trade server return codes
# ─────────────────────────────────────────────────────────────────────

TRADE_RETCODE_DONE: int
"""Request completed."""

TRADE_RETCODE_PLACED: int
"""Request placed for processing."""

TRADE_RETCODE_CANCELED: int
"""Request canceled."""

TRADE_RETCODE_PARTIAL: int
"""Request partially completed."""

TRADE_RETCODE_NO_MONEY: int
"""Not enough money to complete the request."""

TRADE_RETCODE_PRICE_CHANGED: int
"""Price changed, no re-quote."""

TRADE_RETCODE_PRICE_OFF: int
"""There is no price for re-quote."""

TRADE_RETCODE_INVALID: int
"""Invalid request."""

TRADE_RETCODE_INVALID_VOLUME: int
"""Invalid volume in the request."""

TRADE_RETCODE_INVALID_PRICE: int
"""Invalid price in the request."""

TRADE_RETCODE_INVALID_STOPS: int
"""Invalid stops in the request."""

TRADE_RETCODE_TRADE_DISABLED: int
"""Trade is disabled."""

TRADE_RETCODE_MARKET_CLOSED: int
"""Market is closed."""

TRADE_RETCODE_NO_SUPPORT: int
"""The request is not supported by the server."""

TRADE_RETCODE_BUSY: int
"""The server is busy."""

TRADE_RETCODE_NO_CHANGES: int
"""No changes in the request to be applied."""

TRADE_RETCODE_SERVER_DISABLES_AT: int
"""The server's AutoTrading system disabled the authorization of the EA's trade request."""

TRADE_RETCODE_CLIENT_DISABLES_AT: int
"""The client's terminal disabled the authorization of the EA's trade request."""

TRADE_RETCODE_LOCKED: int
"""The request is locked for processing. Please try again later."""

TRADE_RETCODE_FROZEN: int
"""The order or position is frozen."""

TRADE_RETCODE_INVALID_FILL: int
"""The filling type is not allowed by the server."""

TRADE_RETCODE_NO_ACCOUNT: int
"""The account was disconnected."""

TRADE_RETCODE_ONLY_SERVER: int
"""The request can only be processed by the trading server."""

TRADE_RETCODE_LIMIT_ORDERS: int
"""The number of pending orders has reached the limit."""

TRADE_RETCODE_LIMIT_VOLUME: int
"""The volume of open positions and pending orders has reached the limit."""

# ─────────────────────────────────────────────────────────────────────
# TIMEFRAME – Timeframes for chart data
# ─────────────────────────────────────────────────────────────────────

TIMEFRAME_M1: int
"""1 minute."""

TIMEFRAME_M2: int
"""2 minutes."""

TIMEFRAME_M3: int
"""3 minutes."""

TIMEFRAME_M4: int
"""4 minutes."""

TIMEFRAME_M5: int
"""5 minutes."""

TIMEFRAME_M6: int
"""6 minutes (10 minutes in MT5)."""

TIMEFRAME_M10: int
"""10 minutes."""

TIMEFRAME_M12: int
"""12 minutes."""

TIMEFRAME_M15: int
"""15 minutes."""

TIMEFRAME_M20: int
"""20 minutes."""

TIMEFRAME_M30: int
"""30 minutes."""

TIMEFRAME_H1: int
"""1 hour."""

TIMEFRAME_H2: int
"""2 hours."""

TIMEFRAME_H3: int
"""3 hours."""

TIMEFRAME_H4: int
"""4 hours."""

TIMEFRAME_H6: int
"""6 hours."""

TIMEFRAME_H8: int
"""8 hours."""

TIMEFRAME_H12: int
"""12 hours."""

TIMEFRAME_D1: int
"""1 day."""

TIMEFRAME_W1: int
"""1 week."""

TIMEFRAME_MN1: int
"""1 month."""

# ─────────────────────────────────────────────────────────────────────
# COPY_TICKS – Flags for copying ticks
# ─────────────────────────────────────────────────────────────────────

COPY_TICKS_ALL: int
"""Copy all ticks."""

COPY_TICKS_INFO: int
"""Copy only ticks with changes in bid and/or ask."""

COPY_TICKS_TRADE: int
"""Copy only ticks with changes in last."""

# ─────────────────────────────────────────────────────────────────────
# TICK_FLAG – Tick flags
# ─────────────────────────────────────────────────────────────────────

TICK_FLAG_BID: int
"""Tick has bid price change."""

TICK_FLAG_ASK: int
"""Tick has ask price change."""

TICK_FLAG_LAST: int
"""Tick has last price change."""

TICK_FLAG_VOLUME: int
"""Tick has volume change."""

TICK_FLAG_BUY: int
"""Tick was generated as a result of a Buy deal."""

TICK_FLAG_SELL: int
"""Tick was generated as a result of a Sell deal."""

# ─────────────────────────────────────────────────────────────────────
# BOOK_TYPE – Depth of Market order types (ENUM_BOOK_TYPE)
# ─────────────────────────────────────────────────────────────────────

BOOK_TYPE_BUY: int
"""Buy order in the DOM."""

BOOK_TYPE_SELL: int
"""Sell order in the DOM."""

# ─────────────────────────────────────────────────────────────────────
# DEAL_TYPE – Types of deals (ENUM_DEAL_TYPE)
# ─────────────────────────────────────────────────────────────────────

DEAL_TYPE_BUY: int
"""Buy."""

DEAL_TYPE_SELL: int
"""Sell."""

DEAL_TYPE_BALANCE: int
"""Balance operation."""

DEAL_TYPE_CREDIT: int
"""Credit operation."""

DEAL_TYPE_CHARGE: int
"""Additional charge."""

DEAL_TYPE_CORRECTION: int
"""Correction."""

DEAL_TYPE_BONUS: int
"""Bonus."""

DEAL_TYPE_COMMISSION: int
"""Additional commission."""

DEAL_TYPE_COMMISSION_DAILY: int
"""Daily commission."""

DEAL_TYPE_COMMISSION_MONTHLY: int
"""Monthly commission."""

DEAL_TYPE_COMMISSION_AGENT_DAILY: int
"""Daily agent commission."""

DEAL_TYPE_COMMISSION_AGENT_MONTHLY: int
"""Monthly agent commission."""

DEAL_TYPE_INTEREST: int
"""Interest rate."""

DEAL_TYPE_BUY_CANCELED: int
"""Canceled buy deal. Previously obtained profit/loss is charged/withdrawn using a separate balance operation."""

DEAL_TYPE_SELL_CANCELED: int
"""Canceled sell deal. Previously obtained profit/loss is charged/withdrawn using a separate balance operation."""

DEAL_DIVIDEND: int
"""Dividend operations."""

DEAL_DIVIDEND_FRANKED: int
"""Franked (non-taxable) dividend operations."""

DEAL_TAX: int
"""Tax charges."""

# ─────────────────────────────────────────────────────────────────────
# POSITION_TYPE – Types of positions (ENUM_POSITION_TYPE)
# ─────────────────────────────────────────────────────────────────────

POSITION_TYPE_BUY: int
"""Buy position."""

POSITION_TYPE_SELL: int
"""Sell position."""

# ─────────────────────────────────────────────────────────────────────
# POSITION_REASON – Reason for opening a position (ENUM_POSITION_REASON)
# ─────────────────────────────────────────────────────────────────────

POSITION_REASON_CLIENT: int
"""The position was opened as a result of activation of an order placed from a desktop terminal."""

POSITION_REASON_MOBILE: int
"""The position was opened as a result of activation of an order placed from a mobile application."""

POSITION_REASON_WEB: int
"""The position was opened as a result of activation of an order placed from the web platform."""

POSITION_REASON_EXPERT: int
"""The position was opened as a result of activation of an order placed from an MQL5 program."""

# ─────────────────────────────────────────────────────────────────────
# DEAL_ENTRY – Deal entry types (ENUM_DEAL_ENTRY)
# ─────────────────────────────────────────────────────────────────────

DEAL_ENTRY_IN: int
"""Entry in – opening a position or adding to an existing one."""

DEAL_ENTRY_OUT: int
"""Entry out – closing a position or reducing an existing one."""

DEAL_ENTRY_INOUT: int
"""Reverse – position reversal (close and open in the opposite direction)."""

DEAL_ENTRY_OUT_BY: int
"""Close a position by an opposite one."""

# ─────────────────────────────────────────────────────────────────────
# DEAL_REASON – Reason for deal execution (ENUM_DEAL_REASON)
# ─────────────────────────────────────────────────────────────────────

DEAL_REASON_CLIENT: int
"""The deal was executed as a result of activation of an order placed from a desktop terminal."""

DEAL_REASON_MOBILE: int
"""The deal was executed as a result of activation of an order placed from a mobile application."""

DEAL_REASON_WEB: int
"""The deal was executed as a result of activation of an order placed from the web platform."""

DEAL_REASON_EXPERT: int
"""The deal was executed as a result of activation of an order placed from an MQL5 program."""

DEAL_REASON_SL: int
"""The deal was executed as a result of Stop Loss activation."""

DEAL_REASON_TP: int
"""The deal was executed as a result of Take Profit activation."""

DEAL_REASON_SO: int
"""The deal was executed as a result of the Stop Out event."""

DEAL_REASON_ROLLOVER: int
"""The deal was executed due to a rollover."""

DEAL_REASON_VMARGIN: int
"""The deal was executed after charging the variation margin."""

DEAL_REASON_SPLIT: int
"""The deal was executed after the split (price reduction) of an instrument, which had an open position during split announcement."""

DEAL_REASON_CORPORATE_ACTION: int
"""The deal was executed as a result of a corporate action (merging or renaming a security, transferring a client to another account, etc.)."""


# ═════════════════════════════════════════════════════════════════════
# Named Tuple Types
# ═════════════════════════════════════════════════════════════════════


class AccountInfo(NamedTuple):
    """Trading account information returned by :func:`account_info`.

    Contains all properties of the current trading account including
    balance, equity, margin, and account settings.
    """

    login: int
    """Account number (login)."""

    trade_mode: int
    """Account trade mode (ENUM_ACCOUNT_TRADE_MODE: 0=demo, 1=real, 2=contest)."""

    leverage: int
    """Account leverage."""

    limit_orders: int
    """Maximum number of active pending orders."""

    margin_so_mode: int
    """Margin call mode (ENUM_ACCOUNT_STOPOUT_MODE: 0=money, 1=percent)."""

    trade_allowed: bool
    """Whether trading is allowed on the account."""

    trade_expert: bool
    """Whether automated trading (EA) is allowed on the account."""

    margin_mode: int
    """Margin calculation mode (ENUM_ACCOUNT_MARGIN_MODE)."""

    currency_digits: int
    """Number of digits for the account currency display."""

    fifo_close: bool
    """Whether FIFO rule (First In First Out) is applied to close positions."""

    balance: float
    """Account balance."""

    credit: float
    """Account credit."""

    profit: float
    """Current profit/loss on open positions."""

    equity: float
    """Account equity (balance + credit + profit)."""

    margin: float
    """Margin used for opened positions."""

    margin_free: float
    """Free margin available to open new positions."""

    margin_level: float
    """Margin level percentage (equity/margin * 100)."""

    margin_so_call: int
    """Margin call level at which the Stop Out is triggered (in percent)."""

    margin_so_so: int
    """Stop Out level at which positions start to close (in percent)."""

    margin_initial: float
    """Initial margin for opening positions."""

    margin_maintenance: float
    """Maintenance margin."""

    assets: float
    """Current account assets."""

    liabilities: float
    """Current account liabilities."""

    commission_blocked: float
    """Blocked commission amount."""

    name: str
    """Account holder name."""

    server: str
    """Trade server name."""

    currency: str
    """Account currency."""

    company: str
    """Company name of the broker."""


class Tick(NamedTuple):
    """Symbol tick data returned by :func:`symbol_info_tick` and others.

    Contains the latest tick data for a financial instrument.
    """

    time: int
    """Last tick time as a Unix timestamp (seconds since 1970-01-01)."""

    bid: float
    """Current Bid price."""

    ask: float
    """Current Ask price."""

    last: float
    """Price of the last deal (Last)."""

    volume: float
    """Volume of the last deal."""

    time_msc: int
    """Last tick time in milliseconds since 1970-01-01."""

    flags: int
    """Tick flags (combination of TICK_FLAG_*)."""

    volume_real: float
    """Volume of the last deal with float precision."""


class SymbolInfo(NamedTuple):
    """Financial instrument properties returned by :func:`symbol_info`.

    Contains all data obtainable via SymbolInfoInteger(),
    SymbolInfoDouble(), and SymbolInfoString() in one call.
    """

    custom: bool
    """Whether the symbol is custom (non-standard)."""

    chart_mode: int
    """Price chart drawing mode."""

    select: bool
    """Whether the symbol is selected in MarketWatch."""

    visible: bool
    """Whether the symbol is visible in MarketWatch."""

    session_deals: int
    """Number of deals in the current session."""

    session_buy_orders: int
    """Number of Buy orders in the current session."""

    session_sell_orders: int
    """Number of Sell orders in the current session."""

    volume: int
    """Last deal volume."""

    volumehigh: int
    """Maximum deal volume for the day."""

    volumelow: int
    """Minimum deal volume for the day."""

    time: int
    """Time of the last quote."""

    digits: int
    """Number of decimal places in the symbol price."""

    spread: int
    """Current spread in points."""

    spread_float: bool
    """Whether the spread is floating."""

    ticks_bookdepth: int
    """Number of levels displayed in the Depth of Market."""

    trade_calc_mode: int
    """Symbol trade calculation mode (ENUM_SYMBOL_TRADE_CALC_MODE)."""

    trade_mode: int
    """Trade execution mode for the symbol (ENUM_SYMBOL_TRADE_MODE)."""

    start_time: int
    """Trading session start time (seconds from midnight)."""

    expiration_time: int
    """Trading session expiration time (seconds from midnight)."""

    trade_stops_level: int
    """Minimum stop distance in points."""

    trade_freeze_level: int
    """Trade freeze level in points."""

    trade_exemode: int
    """Trade execution mode (ENUM_SYMBOL_TRADE_EXECUTION)."""

    swap_mode: int
    """Swap calculation mode (ENUM_SYMBOL_SWAP_MODE)."""

    swap_rollover3days: int
    """Day of the week for triple swap."""

    margin_hedged_use_leg: bool
    """Whether the margin is calculated using the leg."""

    expiration_mode: int
    """Allowed expiration modes (combination of flags)."""

    filling_mode: int
    """Allowed filling modes (combination of SYMBOL_FILLING_* flags)."""

    order_mode: int
    """Allowed order types (combination of flags)."""

    order_gtc_mode: int
    """GTC (Good Till Cancel) mode for pending orders."""

    option_mode: int
    """Option mode (ENUM_SYMBOL_OPTION_MODE)."""

    option_right: int
    """Option right type (ENUM_SYMBOL_OPTION_RIGHT)."""

    bid: float
    """Current Bid price."""

    bidhigh: float
    """Highest Bid price of the day."""

    bidlow: float
    """Lowest Bid price of the day."""

    ask: float
    """Current Ask price."""

    askhigh: float
    """Highest Ask price of the day."""

    asklow: float
    """Lowest Ask price of the day."""

    last: float
    """Price of the last deal (Last)."""

    lasthigh: float
    """Highest Last price of the day."""

    lastlow: float
    """Lowest Last price of the day."""

    volume_real: float
    """Last deal volume with float precision."""

    volumehigh_real: float
    """Maximum deal volume of the day with float precision."""

    volumelow_real: float
    """Minimum deal volume of the day with float precision."""

    option_strike: float
    """Option strike price."""

    point: float
    """Symbol point size (1 point = 10^(-digits) in price)."""

    trade_tick_value: float
    """Value of 1 tick in the deposit currency."""

    trade_tick_value_profit: float
    """Value of 1 tick for a long position in the deposit currency."""

    trade_tick_value_loss: float
    """Value of 1 tick for a short position in the deposit currency."""

    trade_tick_size: float
    """Minimum price change in points."""

    trade_contract_size: float
    """Contract size in units of the base currency."""

    trade_accrued_interest: float
    """Accrued interest."""

    trade_face_value: float
    """Face value."""

    trade_liquidity_rate: float
    """Liquidity rate."""

    volume_min: float
    """Minimum volume for a trade."""

    volume_max: float
    """Maximum volume for a trade."""

    volume_step: float
    """Volume step (minimum volume increment)."""

    volume_limit: float
    """Maximum volume for a single order."""

    swap_long: float
    """Swap rate for long positions."""

    swap_short: float
    """Swap rate for short positions."""

    margin_initial: float
    """Initial margin for opening positions."""

    margin_maintenance: float
    """Maintenance margin for keeping positions."""

    session_volume: float
    """Total volume of deals in the current session."""

    session_turnover: float
    """Total turnover in the current session."""

    session_interest: float
    """Total open interest in the current session."""

    session_buy_orders_volume: float
    """Total volume of Buy orders in the DOM."""

    session_sell_orders_volume: float
    """Total volume of Sell orders in the DOM."""

    session_open: float
    """Session opening price."""

    session_close: float
    """Session closing price."""

    session_aw: float
    """Session average weighted price."""

    session_price_settlement: float
    """Session settlement price."""

    session_price_limit_min: float
    """Minimum price for the session."""

    session_price_limit_max: float
    """Maximum price for the session."""

    margin_hedged: float
    """Hedged margin for a contract."""

    price_change: float
    """Price change for the day."""

    price_volatility: float
    """Price volatility for the day."""

    price_theoretical: float
    """Theoretical option price."""

    price_greeks_delta: float
    """Option Greeks Delta."""

    price_greeks_theta: float
    """Option Greeks Theta."""

    price_greeks_gamma: float
    """Option Greeks Gamma."""

    price_greeks_vega: float
    """Option Greeks Vega."""

    price_greeks_rho: float
    """Option Greeks Rho."""

    price_greeks_omega: float
    """Option Greeks Omega."""

    price_sensitivity: float
    """Option price sensitivity."""

    basis: str
    """Underlying asset of a futures contract."""

    category: str
    """Category of the symbol."""

    currency_base: str
    """Base currency of the symbol."""

    currency_profit: str
    """Profit currency of the symbol."""

    currency_margin: str
    """Margin currency of the symbol."""

    bank: str
    """Bank that provides quotes."""

    description: str
    """Description of the symbol."""

    exchange: str
    """Exchange name."""

    formula: str
    """Price formula for the symbol."""

    isin: str
    """International Securities Identification Number."""

    name: str
    """Symbol name."""

    page: str
    """Web page with information about the symbol."""

    path: str
    """Path to the symbol in the terminal's data folder."""


class TerminalInfo(NamedTuple):
    """Terminal information returned by :func:`terminal_info`.

    Contains properties of the MetaTrader 5 terminal.
    """

    community_account: bool
    """Whether the MQL5.community account is connected."""

    community_connection: bool
    """Whether MQL5.community connection is active."""

    connected: bool
    """Whether the terminal is connected to the trade server."""

    dlls_allowed: bool
    """Whether DLL import is allowed."""

    trade_allowed: bool
    """Whether trading from the terminal is allowed."""

    tradeapi_disabled: bool
    """Whether the trading API is disabled."""

    email_enabled: bool
    """Whether email notification is enabled."""

    ftp_enabled: bool
    """Whether FTP upload is enabled."""

    notifications_enabled: bool
    """Whether push notifications are enabled."""

    mqid: bool
    """Whether MQL5 identification is enabled."""

    build: int
    """Terminal build number."""

    maxbars: int
    """Maximum number of bars in a chart."""

    codepage: int
    """Terminal code page (character encoding)."""

    ping_last: int
    """Last ping to the server in milliseconds."""

    community_balance: float
    """MQL5.community account balance."""

    retransmission: float
    """Retransmission time factor."""

    company: str
    """Company name."""

    name: str
    """Terminal name."""

    language: str
    """Terminal language."""

    path: str
    """Path to the terminal executable."""

    data_path: str
    """Path to the terminal data folder."""

    commondata_path: str
    """Path to the common data folder for all terminals."""


class BookInfo(NamedTuple):
    """Depth of Market entry returned by :func:`market_book_get`.

    Represents a single price level in the order book.
    """

    type: int
    """Order type in the DOM (BOOK_TYPE_BUY or BOOK_TYPE_SELL)."""

    price: float
    """Order price."""

    volume: int
    """Order volume in lots."""

    volume_dbl: float
    """Order volume as a float with full precision."""


class Rate(NamedTuple):
    """OHLCV price bar returned by :func:`copy_rates_from`, :func:`copy_rates_from_pos`, and :func:`copy_rates_range`.

    Represents a single candlestick/bar on the price chart.
    """

    time: int
    """Bar opening time as a Unix timestamp (seconds since 1970-01-01)."""

    open: float
    """Open price."""

    high: float
    """Highest price during the period."""

    low: float
    """Lowest price during the period."""

    close: float
    """Close price."""

    tick_volume: int
    """Tick volume (number of ticks during the period)."""

    spread: int
    """Spread in points at the bar close time."""

    real_volume: int
    """Real volume (exchange volume, if available)."""


class Order(NamedTuple):
    """Trade order returned by :func:`orders_get`, :func:`history_orders_get`, and others.

    Contains all properties of a trade order (active or historical).
    """

    ticket: int
    """Order ticket (unique identifier)."""

    time_setup: int
    """Order setup time as a Unix timestamp."""

    time_expiration: int
    """Order expiration time as a Unix timestamp."""

    time_done: int
    """Order execution or cancellation time as a Unix timestamp."""

    time_setup_msc: int
    """Order setup time in milliseconds since 1970-01-01."""

    time_done_msc: int
    """Order execution/cancellation time in milliseconds since 1970-01-01."""

    type: int
    """Order type (ENUM_ORDER_TYPE)."""

    type_time: int
    """Order lifetime (ENUM_ORDER_TYPE_TIME)."""

    type_filling: int
    """Order filling policy (ENUM_ORDER_TYPE_FILLING)."""

    type_reason: int
    """Reason for placing the order (ENUM_ORDER_REASON)."""

    status: int
    """Order state (ENUM_ORDER_STATE)."""

    magic: int
    """Magic number (ID of the Expert Advisor that placed the order)."""

    position_id: int
    """Position identifier that the order is associated with after execution."""

    position_by_id: int
    """Identifier of an opposite position used for closing by ORDER_TYPE_CLOSE_BY."""

    magic_identifier: str
    """Unique identifier of the EA's order chain."""

    symbol: str
    """Symbol of the order."""

    volume: float
    """Order initial volume."""

    price_open: float
    """Price specified in the order."""

    price_current: float
    """Current price of the order symbol."""

    sl: float
    """Stop Loss level."""

    tp: float
    """Take Profit level."""

    price_stoplimit: float
    """Limit order price for the StopLimit order."""

    deal: int
    """Deal ticket that closed the order."""

    deal_current: int
    """Deal ticket that is currently processing the order."""

    volume_current: float
    """Current volume of the order (may differ from volume due to partial fills)."""

    price_distance: float
    """Distance of the order price from the current price."""

    comment: str
    """Order comment."""

    external_id: str
    """Order identifier in an external trading system."""


class Deal(NamedTuple):
    """Historical deal returned by :func:`history_deals_get`.

    Contains all properties of an executed trade (deal).
    """

    ticket: int
    """Deal ticket (unique identifier)."""

    order: int
    """Ticket of the order that initiated this deal."""

    time: int
    """Deal execution time as a Unix timestamp."""

    time_msc: int
    """Deal execution time in milliseconds since 1970-01-01."""

    type: int
    """Deal type (ENUM_DEAL_TYPE)."""

    entry: int
    """Deal entry type (ENUM_DEAL_ENTRY: entry in, entry out, reverse, etc.)."""

    magic: int
    """Magic number of the deal."""

    position_id: int
    """Position identifier the deal belongs to."""

    reason: int
    """Reason for deal execution (ENUM_DEAL_REASON)."""

    exchange: int
    """Exchange identifier."""

    deal_id: int
    """Deal identifier for linking related deals."""

    order_external_id: str
    """External order identifier."""

    deal_external_id: str
    """External deal identifier."""

    symbol: str
    """Deal symbol."""

    volume: float
    """Deal volume."""

    price: float
    """Deal execution price."""

    commission: float
    """Commission charged."""

    swap: float
    """Cumulative swap on close."""

    profit: float
    """Deal profit/loss."""

    volume_fee: float
    """Fee for making a deal charged immediately after performing a deal."""

    price_sl: float
    """Stop Loss level at the time of deal execution."""

    price_tp: float
    """Take Profit level at the time of deal execution."""

    comment: str
    """Deal comment."""


class Position(NamedTuple):
    """Open position returned by :func:`positions_get`.

    Contains all properties of an open trading position.
    """

    ticket: int
    """Position ticket (unique identifier)."""

    time: int
    """Position open time as a Unix timestamp."""

    time_msc: int
    """Position opening time in milliseconds since 1970-01-01."""

    time_update: int
    """Position changing time as a Unix timestamp."""

    time_update_msc: int
    """Position changing time in milliseconds since 1970-01-01."""

    identifier: int
    """Position identifier (unique number assigned to each re-opened position, does not change)."""

    magic: int
    """Magic number of the position."""

    reason: int
    """Reason for opening a position (ENUM_POSITION_REASON)."""

    volume: float
    """Position volume."""

    price_open: float
    """Position open price."""

    sl: float
    """Stop Loss level of the opened position."""

    tp: float
    """Take Profit level of the opened position."""

    price_current: float
    """Current price of the position symbol."""

    swap: float
    """Cumulative swap."""

    profit: float
    """Current profit/loss."""

    symbol: str
    """Symbol of the position."""

    comment: str
    """Position comment."""

    external_id: str
    """Position identifier in an external trading system."""

    type: int
    """Position type (ENUM_POSITION_TYPE: POSITION_TYPE_BUY or POSITION_TYPE_SELL)."""


class TradeRequest(NamedTuple):
    """Trade request structure used as input for :func:`order_check` and :func:`order_send`.

    Contains all parameters needed for a trade operation.
    """

    action: int
    """Type of trade operation (TRADE_ACTION_*)."""

    magic: int
    """Magic number of the Expert Advisor."""

    order: int
    """Order ticket (for TRADE_ACTION_MODIFY and TRADE_ACTION_REMOVE)."""

    symbol: str
    """Symbol for the trade operation."""

    volume: float
    """Volume of the trade operation in lots."""

    price: float
    """Price for the trade operation."""

    stoplimit: float
    """StopLimit price for StopLimit orders."""

    sl: float
    """Stop Loss level."""

    tp: float
    """Take Profit level."""

    deviation: int
    """Maximum allowed deviation from the requested price in points."""

    type: int
    """Order type (ORDER_TYPE_BUY, ORDER_TYPE_SELL, etc.)."""

    type_filling: int
    """Order filling policy (ORDER_FILLING_*)."""

    type_time: int
    """Order lifetime (ORDER_TIME_*)."""

    expiration: int
    """Order expiration time as a Unix timestamp (for ORDER_TIME_SPECIFIED)."""

    comment: str
    """Comment for the trade request."""

    position: int
    """Position ticket (for TRADE_ACTION_SLTP and TRADE_ACTION_CLOSE_BY)."""

    position_by: int
    """Opposite position ticket (for TRADE_ACTION_CLOSE_BY)."""


class TradeOrderResult(NamedTuple):
    """Result of a trade operation returned by :func:`order_check` and :func:`order_send`.

    Contains the server response after processing a trade request.
    """

    order: int
    """Order ticket of the placed/executed order."""

    deal: int
    """Deal ticket (if an immediate execution resulted in a deal)."""

    volume: float
    """Volume of the placed order."""

    price: float
    """Price at which the order was executed."""

    bid: float
    """Bid price at the time of execution."""

    ask: float
    """Ask price at the time of execution."""

    comment: str
    """Server comment for the trade operation."""

    request_id: int
    """Request identifier (unique ID assigned by the terminal)."""

    retcode: int
    """Return code of the trade server (TRADE_RETCODE_*)."""

    deal_current: float
    """Current deal ticket (for partially executed orders)."""

    volume_current: float
    """Volume of the currently executed part."""

    request: TradeRequest
    """The original trade request that was sent to the server."""


# ═════════════════════════════════════════════════════════════════════
# Functions
# ═════════════════════════════════════════════════════════════════════


def initialize(
    path: str = ...,
    login: int = ...,
    password: str = ...,
    server: str = ...,
    timeout: int = ...,
    portable: bool = ...,
) -> bool:
    """Initialize connection to the MetaTrader 5 terminal.

    The function connects to the trading terminal and initializes the
    interface for data exchange. If the path is not specified, the
    function connects to the terminal running in the current directory.

    Args:
        path: Path to the MetaTrader 5 terminal executable. If not
            specified, uses the current directory.
        login: Trading account number. If not specified, uses the
            last successful login.
        password: Trading account password. If not specified, uses
            the last successful password.
        server: Trade server name. If not specified, uses the
            last successful server.
        timeout: Connection timeout in milliseconds. Default is 60000.
        portable: If True, run the terminal in portable mode.

    Returns:
        True if initialization was successful, False otherwise.
        Use :func:`last_error` to get error details.
    """
    ...


def shutdown() -> None:
    """Shutdown connection to the MetaTrader 5 terminal.

    The function disconnects from the trading terminal and releases
    all allocated resources. It is recommended to call this function
    at the end of the program.
    """
    ...


def login(
    login: int,
    password: str = ...,
    server: str = ...,
    timeout: int = ...,
) -> bool:
    """Log in to a trading account.

    The function allows logging in to a trading account without
    re-initializing the connection. This is useful when switching
    between accounts.

    Args:
        login: Trading account number.
        password: Trading account password. Default is empty string.
        server: Trade server name. Default is empty string.
        timeout: Connection timeout in milliseconds. Default is 60000.

    Returns:
        True if login was successful, False otherwise.
        Use :func:`last_error` to get error details.
    """
    ...


def version() -> list[Any]:
    """Get the MetaTrader 5 package version.

    Returns:
        A list containing [major_version, minor_version, revision,
        build]. For example: [5, 0, 30, 2455].
    """
    ...


def last_error() -> tuple[int, str]:
    """Get the last error that occurred in the package.

    The function returns the error code and a textual description
    of the last error that occurred during the execution of any
    function of the package.

    Returns:
        A tuple of (error_code, description). error_code is an
        integer error code, description is a human-readable string.
    """
    ...


def account_info() -> AccountInfo | None:
    """Get data on the current trading account.

    Returns an :class:`AccountInfo` named tuple with all account
    properties, or None if an error occurred.

    Returns:
        An :class:`AccountInfo` named tuple, or None on error.
    """
    ...


def terminal_info() -> TerminalInfo | None:
    """Get data on the MetaTrader 5 terminal.

    Returns a :class:`TerminalInfo` named tuple with all terminal
    properties, or None if an error occurred.

    Returns:
        A :class:`TerminalInfo` named tuple, or None on error.
    """
    ...


def symbols_total() -> int:
    """Get the total number of financial instruments in the terminal.

    Returns:
        The total number of symbols available in the terminal.
    """
    ...


@overload
def symbols_get() -> tuple[SymbolInfo, ...] | None:
    """Get all financial instruments.

    Returns information about all symbols available in the terminal.

    Returns:
        A tuple of :class:`SymbolInfo` named tuples, or None on error.
    """
    ...

@overload
def symbols_get(group: str) -> tuple[SymbolInfo, ...] | None:
    """Get financial instruments matching a group filter.

    Args:
        group: Group name for filtering. Can use wildcards.
            Examples: "Forex", "*,Gold", "*.*EUR".

    Returns:
        A tuple of :class:`SymbolInfo` named tuples, or None on error.
    """
    ...


def symbol_info(symbol: str) -> SymbolInfo | None:
    """Get data on the specified financial instrument.

    Returns all data obtainable via SymbolInfoInteger(),
    SymbolInfoDouble(), and SymbolInfoString() in one call.

    Args:
        symbol: Financial instrument name (e.g., "EURUSD").

    Returns:
        A :class:`SymbolInfo` named tuple, or None on error.
    """
    ...


def symbol_info_tick(symbol: str) -> Tick | None:
    """Get the last tick for the specified symbol.

    Args:
        symbol: Financial instrument name (e.g., "EURUSD").

    Returns:
        A :class:`Tick` named tuple with the latest tick data,
        or None on error.
    """
    ...


def symbol_select(symbol: str, enable: bool = ...) -> bool:
    """Enable or disable a symbol in MarketWatch.

    The function allows adding or removing a symbol from MarketWatch.
    Some symbols may not be visible by default.

    Args:
        symbol: Financial instrument name.
        enable: If True, enable the symbol in MarketWatch.
            If False, disable it.

    Returns:
        True if the operation was successful, False otherwise.
    """
    ...


def market_book_add(symbol: str) -> bool:
    """Subscribe to the Depth of Market for a symbol.

    The function enables receiving DOM data (Level 2 quotes) for
    the specified symbol.

    Args:
        symbol: Financial instrument name.

    Returns:
        True if the subscription was successful, False otherwise.
    """
    ...


def market_book_get(symbol: str) -> tuple[BookInfo, ...] | None:
    """Get the current Depth of Market data.

    The function returns the current DOM (Level 2) data for a symbol.
    Must be called after :func:`market_book_add`.

    Args:
        symbol: Financial instrument name.

    Returns:
        A tuple of :class:`BookInfo` named tuples representing DOM
        entries, or None on error.
    """
    ...


def market_book_release(symbol: str) -> bool:
    """Unsubscribe from the Depth of Market.

    The function stops receiving DOM data for the specified symbol.

    Args:
        symbol: Financial instrument name.

    Returns:
        True if the operation was successful, False otherwise.
    """
    ...


def copy_rates_from(
    symbol: str,
    timeframe: int,
    date_from: datetime | int,
    count: int,
) -> np.ndarray | None:
    """Copy N rates starting from the specified date.

    The function copies ``count`` bars of price data starting from
    the specified date/time.

    Args:
        symbol: Financial instrument name.
        timeframe: Timeframe (TIMEFRAME_* constant).
        date_from: Start date/time as a datetime object or Unix timestamp.
        count: Number of bars to copy.

    Returns:
        A numpy structured array with columns: time, open, high, low,
        close, tick_volume, spread, real_volume. Returns None on error.
    """
    ...


def copy_rates_from_pos(
    symbol: str,
    timeframe: int,
    start_pos: int,
    count: int,
) -> np.ndarray | None:
    """Copy N rates starting from the specified position.

    The function copies ``count`` bars starting from position
    ``start_pos`` (0 = most recent bar).

    Args:
        symbol: Financial instrument name.
        timeframe: Timeframe (TIMEFRAME_* constant).
        start_pos: Start position (0 = current bar, 1 = one bar back, etc.).
        count: Number of bars to copy.

    Returns:
        A numpy structured array with columns: time, open, high, low,
        close, tick_volume, spread, real_volume. Returns None on error.
    """
    ...


def copy_rates_range(
    symbol: str,
    timeframe: int,
    date_from: datetime | int,
    date_to: datetime | int,
) -> np.ndarray | None:
    """Copy rates for the specified time range.

    The function copies all bars between ``date_from`` and ``date_to``.

    Args:
        symbol: Financial instrument name.
        timeframe: Timeframe (TIMEFRAME_* constant).
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.

    Returns:
        A numpy structured array with columns: time, open, high, low,
        close, tick_volume, spread, real_volume. Returns None on error.
    """
    ...


def copy_ticks_from(
    symbol: str,
    date_from: datetime | int,
    count: int,
    flags: int,
) -> np.ndarray | None:
    """Copy N ticks starting from the specified date.

    The function copies ``count`` ticks starting from the specified
    date/time.

    Args:
        symbol: Financial instrument name.
        date_from: Start date/time as a datetime object or Unix timestamp.
        count: Number of ticks to copy.
        flags: Tick copying flags (COPY_TICKS_ALL, COPY_TICKS_INFO,
            or COPY_TICKS_TRADE).

    Returns:
        A numpy structured array with columns: time, bid, ask, last,
        volume, time_msc, flags, volume_real. Returns None on error.
    """
    ...


def copy_ticks_range(
    symbol: str,
    date_from: datetime | int,
    date_to: datetime | int,
    flags: int,
) -> np.ndarray | None:
    """Copy ticks for the specified time range.

    The function copies all ticks between ``date_from`` and ``date_to``.

    Args:
        symbol: Financial instrument name.
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.
        flags: Tick copying flags (COPY_TICKS_ALL, COPY_TICKS_INFO,
            or COPY_TICKS_TRADE).

    Returns:
        A numpy structured array with columns: time, bid, ask, last,
        volume, time_msc, flags, volume_real. Returns None on error.
    """
    ...


def orders_total() -> int:
    """Get the total number of active orders.

    Returns:
        The total number of active (unfilled) pending orders.
    """
    ...


@overload
def orders_get() -> tuple[Order, ...] | None:
    """Get all active orders.

    Returns:
        A tuple of :class:`Order` named tuples for all active orders,
        or None on error.
    """
    ...

@overload
def orders_get(*, symbol: str) -> tuple[Order, ...] | None:
    """Get active orders for a specific symbol.

    Args:
        symbol: Financial instrument name.

    Returns:
        A tuple of :class:`Order` named tuples, or None on error.
    """
    ...

@overload
def orders_get(*, group: str) -> tuple[Order, ...] | None:
    """Get active orders matching a group filter.

    Args:
        group: Group name for filtering (e.g., "*,EURUSD").

    Returns:
        A tuple of :class:`Order` named tuples, or None on error.
    """
    ...

@overload
def orders_get(*, ticket: int) -> tuple[Order, ...] | None:
    """Get an active order by its ticket.

    Args:
        ticket: Order ticket number.

    Returns:
        A tuple of :class:`Order` named tuples (single element),
        or None if not found.
    """
    ...


def order_calc_margin(
    action: int,
    symbol: str,
    volume: float,
    price: float,
) -> float | None:
    """Calculate margin required for a trade operation.

    The function calculates the margin that will be used for a
    trade operation with the specified parameters.

    Args:
        action: Trade operation type (ORDER_TYPE_BUY or ORDER_TYPE_SELL).
        symbol: Financial instrument name.
        volume: Trade volume in lots.
        price: Price at which the trade will be executed.

    Returns:
        The required margin amount, or None on error.
    """
    ...


def order_calc_profit(
    action: int,
    symbol: str,
    volume: float,
    price_open: float,
    price_close: float,
) -> float | None:
    """Calculate profit/loss for a trade operation.

    The function calculates the profit/loss that would result from
    a trade operation with the specified parameters.

    Args:
        action: Trade operation type (ORDER_TYPE_BUY or ORDER_TYPE_SELL).
        symbol: Financial instrument name.
        volume: Trade volume in lots.
        price_open: Opening price of the trade.
        price_close: Closing price of the trade.

    Returns:
        The calculated profit/loss amount, or None on error.
    """
    ...


def order_check(request: dict[str, Any]) -> TradeOrderResult | None:
    """Check a trade request without sending it.

    The function checks a trade request and returns the result
    without actually sending it to the server. This allows checking
    whether a trade request can be processed.

    Args:
        request: A dictionary containing trade request fields
            (see :class:`TradeRequest` for field names).

    Returns:
        A :class:`TradeOrderResult` named tuple with the check result,
        or None on error.
    """
    ...


def order_send(request: dict[str, Any]) -> TradeOrderResult | None:
    """Send a trade request to the server.

    The function sends a trade request to the server for execution.
    For market orders, the trade is executed immediately.
    For pending orders, the order is placed and waits for activation.

    Args:
        request: A dictionary containing trade request fields
            (see :class:`TradeRequest` for field names).

    Returns:
        A :class:`TradeOrderResult` named tuple with the execution
        result, or None on error.
    """
    ...


def positions_total() -> int:
    """Get the total number of open positions.

    Returns:
        The total number of currently open positions.
    """
    ...


@overload
def positions_get() -> tuple[Position, ...] | None:
    """Get all open positions.

    Returns:
        A tuple of :class:`Position` named tuples for all open
        positions, or None on error.
    """
    ...

@overload
def positions_get(*, symbol: str) -> tuple[Position, ...] | None:
    """Get open positions for a specific symbol.

    Args:
        symbol: Financial instrument name.

    Returns:
        A tuple of :class:`Position` named tuples, or None on error.
    """
    ...

@overload
def positions_get(*, group: str) -> tuple[Position, ...] | None:
    """Get open positions matching a group filter.

    Args:
        group: Group name for filtering (e.g., "*,EURUSD").

    Returns:
        A tuple of :class:`Position` named tuples, or None on error.
    """
    ...

@overload
def positions_get(*, ticket: int) -> tuple[Position, ...] | None:
    """Get an open position by its ticket.

    Args:
        ticket: Position ticket number.

    Returns:
        A tuple of :class:`Position` named tuples (single element),
        or None if not found.
    """
    ...


def history_orders_total(
    date_from: datetime | int,
    date_to: datetime | int,
) -> int:
    """Get the total number of orders in the history for a time range.

    Args:
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.

    Returns:
        The total number of orders in the specified time range.
    """
    ...


@overload
def history_orders_get(
    date_from: datetime | int,
    date_to: datetime | int,
    group: str = ...,
) -> tuple[Order, ...] | None:
    """Get historical orders for a time range.

    Args:
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.
        group: Optional group filter for symbols.

    Returns:
        A tuple of :class:`Order` named tuples, or None on error.
    """
    ...

@overload
def history_orders_get(
    *,
    ticket: int,
) -> tuple[Order, ...] | None:
    """Get a historical order by its ticket.

    Args:
        ticket: Order ticket number.

    Returns:
        A tuple of :class:`Order` named tuples (single element),
        or None if not found.
    """
    ...

@overload
def history_orders_get(
    *,
    position: int,
) -> tuple[Order, ...] | None:
    """Get all historical orders related to a position.

    Args:
        position: Position identifier.

    Returns:
        A tuple of :class:`Order` named tuples, or None on error.
    """
    ...


def history_deals_total(
    date_from: datetime | int,
    date_to: datetime | int,
) -> int:
    """Get the total number of deals in the history for a time range.

    Args:
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.

    Returns:
        The total number of deals in the specified time range.
    """
    ...


@overload
def history_deals_get(
    date_from: datetime | int,
    date_to: datetime | int,
    group: str = ...,
) -> tuple[Deal, ...] | None:
    """Get historical deals for a time range.

    Args:
        date_from: Start date/time as a datetime object or Unix timestamp.
        date_to: End date/time as a datetime object or Unix timestamp.
        group: Optional group filter for symbols.

    Returns:
        A tuple of :class:`Deal` named tuples, or None on error.
    """
    ...

@overload
def history_deals_get(
    *,
    ticket: int,
) -> tuple[Deal, ...] | None:
    """Get a historical deal by its ticket.

    Args:
        ticket: Deal ticket number.

    Returns:
        A tuple of :class:`Deal` named tuples (single element),
        or None if not found.
    """
    ...

@overload
def history_deals_get(
    *,
    position: int,
) -> tuple[Deal, ...] | None:
    """Get all historical deals related to a position.

    Args:
        position: Position identifier.

    Returns:
        A tuple of :class:`Deal` named tuples, or None on error.
    """
    ...
