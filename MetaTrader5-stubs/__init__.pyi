from typing import TypedDict,NamedTuple,Final
import numpy as np

# --- module metadata ---
__version__: Final[str] = "5.0.5735"
__author__: Final[str] = "MetaQuotes Ltd."

# --- timeframes ---
TIMEFRAME_M1: Final[int] = 1
TIMEFRAME_M2: Final[int] = 2
TIMEFRAME_M3: Final[int] = 3
TIMEFRAME_M4: Final[int] = 4
TIMEFRAME_M5: Final[int] = 5
TIMEFRAME_M6: Final[int] = 6
TIMEFRAME_M10: Final[int] = 10
TIMEFRAME_M12: Final[int] = 12
TIMEFRAME_M15: Final[int] = 15
TIMEFRAME_M20: Final[int] = 20
TIMEFRAME_M30: Final[int] = 30
TIMEFRAME_H1: Final[int] = 1 | 0x4000
TIMEFRAME_H2: Final[int] = 2 | 0x4000
TIMEFRAME_H4: Final[int] = 4 | 0x4000
TIMEFRAME_H3: Final[int] = 3 | 0x4000
TIMEFRAME_H6: Final[int] = 6 | 0x4000
TIMEFRAME_H8: Final[int] = 8 | 0x4000
TIMEFRAME_H12: Final[int] = 12 | 0x4000
TIMEFRAME_D1: Final[int] = 24 | 0x4000
TIMEFRAME_W1: Final[int] = 1 | 0x8000
TIMEFRAME_MN1: Final[int] = 1 | 0xC000

# --- tick copy flags ---
COPY_TICKS_ALL: Final[int] = -1
COPY_TICKS_INFO: Final[int] = 1
COPY_TICKS_TRADE: Final[int] = 2

# --- tick flags ---
TICK_FLAG_BID: Final[int] = 0x02
TICK_FLAG_ASK: Final[int] = 0x04
TICK_FLAG_LAST: Final[int] = 0x08
TICK_FLAG_VOLUME: Final[int] = 0x10
TICK_FLAG_BUY: Final[int] = 0x20
TICK_FLAG_SELL: Final[int] = 0x40

# --- position type, ENUM_POSITION_TYPE ---
POSITION_TYPE_BUY: Final[int] = 0
POSITION_TYPE_SELL: Final[int] = 1

# --- position reason, ENUM_POSITION_REASON ---
POSITION_REASON_CLIENT: Final[int] = 0
POSITION_REASON_MOBILE: Final[int] = 1
POSITION_REASON_WEB: Final[int] = 2
POSITION_REASON_EXPERT: Final[int] = 3

# --- order types, ENUM_ORDER_TYPE ---
ORDER_TYPE_BUY: Final[int] = 0
ORDER_TYPE_SELL: Final[int] = 1
ORDER_TYPE_BUY_LIMIT: Final[int] = 2
ORDER_TYPE_SELL_LIMIT: Final[int] = 3
ORDER_TYPE_BUY_STOP: Final[int] = 4
ORDER_TYPE_SELL_STOP: Final[int] = 5
ORDER_TYPE_BUY_STOP_LIMIT: Final[int] = 6
ORDER_TYPE_SELL_STOP_LIMIT: Final[int] = 7
ORDER_TYPE_CLOSE_BY: Final[int] = 8

# --- order state, ENUM_ORDER_STATE ---
ORDER_STATE_STARTED: Final[int] = 0
ORDER_STATE_PLACED: Final[int] = 1
ORDER_STATE_CANCELED: Final[int] = 2
ORDER_STATE_PARTIAL: Final[int] = 3
ORDER_STATE_FILLED: Final[int] = 4
ORDER_STATE_REJECTED: Final[int] = 5
ORDER_STATE_EXPIRED: Final[int] = 6
ORDER_STATE_REQUEST_ADD: Final[int] = 7
ORDER_STATE_REQUEST_MODIFY: Final[int] = 8
ORDER_STATE_REQUEST_CANCEL: Final[int] = 9

# --- ENUM_ORDER_TYPE_FILLING ---
ORDER_FILLING_FOK: Final[int] = 0
ORDER_FILLING_IOC: Final[int] = 1
ORDER_FILLING_RETURN: Final[int] = 2
ORDER_FILLING_BOC: Final[int] = 3

# --- ENUM_ORDER_TYPE_TIME ---
ORDER_TIME_GTC: Final[int] = 0
ORDER_TIME_DAY: Final[int] = 1
ORDER_TIME_SPECIFIED: Final[int] = 2
ORDER_TIME_SPECIFIED_DAY: Final[int] = 3

# --- ENUM_ORDER_REASON ---
ORDER_REASON_CLIENT: Final[int] = 0
ORDER_REASON_MOBILE: Final[int] = 1
ORDER_REASON_WEB: Final[int] = 2
ORDER_REASON_EXPERT: Final[int] = 3
ORDER_REASON_SL: Final[int] = 4
ORDER_REASON_TP: Final[int] = 5
ORDER_REASON_SO: Final[int] = 6

# --- deal types, ENUM_DEAL_TYPE ---
DEAL_TYPE_BUY: Final[int] = 0
DEAL_TYPE_SELL: Final[int] = 1
DEAL_TYPE_BALANCE: Final[int] = 2
DEAL_TYPE_CREDIT: Final[int] = 3
DEAL_TYPE_CHARGE: Final[int] = 4
DEAL_TYPE_CORRECTION: Final[int] = 5
DEAL_TYPE_BONUS: Final[int] = 6
DEAL_TYPE_COMMISSION: Final[int] = 7
DEAL_TYPE_COMMISSION_DAILY: Final[int] = 8
DEAL_TYPE_COMMISSION_MONTHLY: Final[int] = 9
DEAL_TYPE_COMMISSION_AGENT_DAILY: Final[int] = 10
DEAL_TYPE_COMMISSION_AGENT_MONTHLY: Final[int] = 11
DEAL_TYPE_INTEREST: Final[int] = 12
DEAL_TYPE_BUY_CANCELED: Final[int] = 13
DEAL_TYPE_SELL_CANCELED: Final[int] = 14
DEAL_DIVIDEND: Final[int] = 15
DEAL_DIVIDEND_FRANKED: Final[int] = 16
DEAL_TAX: Final[int] = 17

# --- ENUM_DEAL_ENTRY ---
DEAL_ENTRY_IN: Final[int] = 0
DEAL_ENTRY_OUT: Final[int] = 1
DEAL_ENTRY_INOUT: Final[int] = 2
DEAL_ENTRY_OUT_BY: Final[int] = 3

# --- ENUM_DEAL_REASON ---
DEAL_REASON_CLIENT: Final[int] = 0
DEAL_REASON_MOBILE: Final[int] = 1
DEAL_REASON_WEB: Final[int] = 2
DEAL_REASON_EXPERT: Final[int] = 3
DEAL_REASON_SL: Final[int] = 4
DEAL_REASON_TP: Final[int] = 5
DEAL_REASON_SO: Final[int] = 6
DEAL_REASON_ROLLOVER: Final[int] = 7
DEAL_REASON_VMARGIN: Final[int] = 8
DEAL_REASON_SPLIT: Final[int] = 9

# --- ENUM_TRADE_REQUEST_ACTIONS ---
TRADE_ACTION_DEAL: Final[int] = 1
TRADE_ACTION_PENDING: Final[int] = 5
TRADE_ACTION_SLTP: Final[int] = 6
TRADE_ACTION_MODIFY: Final[int] = 7
TRADE_ACTION_REMOVE: Final[int] = 8
TRADE_ACTION_CLOSE_BY: Final[int] = 10

# --- ENUM_SYMBOL_CHART_MODE ---
SYMBOL_CHART_MODE_BID: Final[int] = 0
SYMBOL_CHART_MODE_LAST: Final[int] = 1

# --- ENUM_SYMBOL_CALC_MODE ---
SYMBOL_CALC_MODE_FOREX: Final[int] = 0
SYMBOL_CALC_MODE_FUTURES: Final[int] = 1
SYMBOL_CALC_MODE_CFD: Final[int] = 2
SYMBOL_CALC_MODE_CFDINDEX: Final[int] = 3
SYMBOL_CALC_MODE_CFDLEVERAGE: Final[int] = 4
SYMBOL_CALC_MODE_FOREX_NO_LEVERAGE: Final[int] = 5
SYMBOL_CALC_MODE_EXCH_STOCKS: Final[int] = 32
SYMBOL_CALC_MODE_EXCH_FUTURES: Final[int] = 33
SYMBOL_CALC_MODE_EXCH_OPTIONS: Final[int] = 34
SYMBOL_CALC_MODE_EXCH_OPTIONS_MARGIN: Final[int] = 36
SYMBOL_CALC_MODE_EXCH_BONDS: Final[int] = 37
SYMBOL_CALC_MODE_EXCH_STOCKS_MOEX: Final[int] = 38
SYMBOL_CALC_MODE_EXCH_BONDS_MOEX: Final[int] = 39
SYMBOL_CALC_MODE_SERV_COLLATERAL: Final[int] = 64

# --- ENUM_SYMBOL_TRADE_MODE ---
SYMBOL_TRADE_MODE_DISABLED: Final[int] = 0
SYMBOL_TRADE_MODE_LONGONLY: Final[int] = 1
SYMBOL_TRADE_MODE_SHORTONLY: Final[int] = 2
SYMBOL_TRADE_MODE_CLOSEONLY: Final[int] = 3
SYMBOL_TRADE_MODE_FULL: Final[int] = 4

# --- ENUM_SYMBOL_TRADE_EXECUTION ---
SYMBOL_TRADE_EXECUTION_REQUEST: Final[int] = 0
SYMBOL_TRADE_EXECUTION_INSTANT: Final[int] = 1
SYMBOL_TRADE_EXECUTION_MARKET: Final[int] = 2
SYMBOL_TRADE_EXECUTION_EXCHANGE: Final[int] = 3

# --- ENUM_SYMBOL_SWAP_MODE ---
SYMBOL_SWAP_MODE_DISABLED: Final[int] = 0
SYMBOL_SWAP_MODE_POINTS: Final[int] = 1
SYMBOL_SWAP_MODE_CURRENCY_SYMBOL: Final[int] = 2
SYMBOL_SWAP_MODE_CURRENCY_MARGIN: Final[int] = 3
SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT: Final[int] = 4
SYMBOL_SWAP_MODE_INTEREST_CURRENT: Final[int] = 5
SYMBOL_SWAP_MODE_INTEREST_OPEN: Final[int] = 6
SYMBOL_SWAP_MODE_REOPEN_CURRENT: Final[int] = 7
SYMBOL_SWAP_MODE_REOPEN_BID: Final[int] = 8

# --- ENUM_DAY_OF_WEEK ---
DAY_OF_WEEK_SUNDAY: Final[int] = 0
DAY_OF_WEEK_MONDAY: Final[int] = 1
DAY_OF_WEEK_TUESDAY: Final[int] = 2
DAY_OF_WEEK_WEDNESDAY: Final[int] = 3
DAY_OF_WEEK_THURSDAY: Final[int] = 4
DAY_OF_WEEK_FRIDAY: Final[int] = 5
DAY_OF_WEEK_SATURDAY: Final[int] = 6

# --- ENUM_SYMBOL_ORDER_GTC_MODE ---
SYMBOL_ORDERS_GTC: Final[int] = 0
SYMBOL_ORDERS_DAILY: Final[int] = 1
SYMBOL_ORDERS_DAILY_NO_STOPS: Final[int] = 2

# --- ENUM_SYMBOL_OPTION_RIGHT ---
SYMBOL_OPTION_RIGHT_CALL: Final[int] = 0
SYMBOL_OPTION_RIGHT_PUT: Final[int] = 1

# --- ENUM_SYMBOL_OPTION_MODE ---
SYMBOL_OPTION_MODE_EUROPEAN: Final[int] = 0
SYMBOL_OPTION_MODE_AMERICAN: Final[int] = 1

# --- ENUM_ACCOUNT_TRADE_MODE ---
ACCOUNT_TRADE_MODE_DEMO: Final[int] = 0
ACCOUNT_TRADE_MODE_CONTEST: Final[int] = 1
ACCOUNT_TRADE_MODE_REAL: Final[int] = 2

# --- ENUM_ACCOUNT_STOPOUT_MODE ---
ACCOUNT_STOPOUT_MODE_PERCENT: Final[int] = 0
ACCOUNT_STOPOUT_MODE_MONEY: Final[int] = 1

# --- ENUM_ACCOUNT_MARGIN_MODE ---
ACCOUNT_MARGIN_MODE_RETAIL_NETTING: Final[int] = 0
ACCOUNT_MARGIN_MODE_EXCHANGE: Final[int] = 1
ACCOUNT_MARGIN_MODE_RETAIL_HEDGING: Final[int] = 2

# --- ENUM_BOOK_TYPE ---
BOOK_TYPE_SELL: Final[int] = 1
BOOK_TYPE_BUY: Final[int] = 2
BOOK_TYPE_SELL_MARKET: Final[int] = 3
BOOK_TYPE_BUY_MARKET: Final[int] = 4

# --- order send/check return codes ---
TRADE_RETCODE_REQUOTE: Final[int] = 10004
TRADE_RETCODE_REJECT: Final[int] = 10006
TRADE_RETCODE_CANCEL: Final[int] = 10007
TRADE_RETCODE_PLACED: Final[int] = 10008
TRADE_RETCODE_DONE: Final[int] = 10009
TRADE_RETCODE_DONE_PARTIAL: Final[int] = 10010
TRADE_RETCODE_ERROR: Final[int] = 10011
TRADE_RETCODE_TIMEOUT: Final[int] = 10012
TRADE_RETCODE_INVALID: Final[int] = 10013
TRADE_RETCODE_INVALID_VOLUME: Final[int] = 10014
TRADE_RETCODE_INVALID_PRICE: Final[int] = 10015
TRADE_RETCODE_INVALID_STOPS: Final[int] = 10016
TRADE_RETCODE_TRADE_DISABLED: Final[int] = 10017
TRADE_RETCODE_MARKET_CLOSED: Final[int] = 10018
TRADE_RETCODE_NO_MONEY: Final[int] = 10019
TRADE_RETCODE_PRICE_CHANGED: Final[int] = 10020
TRADE_RETCODE_PRICE_OFF: Final[int] = 10021
TRADE_RETCODE_INVALID_EXPIRATION: Final[int] = 10022
TRADE_RETCODE_ORDER_CHANGED: Final[int] = 10023
TRADE_RETCODE_TOO_MANY_REQUESTS: Final[int] = 10024
TRADE_RETCODE_NO_CHANGES: Final[int] = 10025
TRADE_RETCODE_SERVER_DISABLES_AT: Final[int] = 10026
TRADE_RETCODE_CLIENT_DISABLES_AT: Final[int] = 10027
TRADE_RETCODE_LOCKED: Final[int] = 10028
TRADE_RETCODE_FROZEN: Final[int] = 10029
TRADE_RETCODE_INVALID_FILL: Final[int] = 10030
TRADE_RETCODE_CONNECTION: Final[int] = 10031
TRADE_RETCODE_ONLY_REAL: Final[int] = 10032
TRADE_RETCODE_LIMIT_ORDERS: Final[int] = 10033
TRADE_RETCODE_LIMIT_VOLUME: Final[int] = 10034
TRADE_RETCODE_INVALID_ORDER: Final[int] = 10035
TRADE_RETCODE_POSITION_CLOSED: Final[int] = 10036
TRADE_RETCODE_INVALID_CLOSE_VOLUME: Final[int] = 10038
TRADE_RETCODE_CLOSE_ORDER_EXIST: Final[int] = 10039
TRADE_RETCODE_LIMIT_POSITIONS: Final[int] = 10040
TRADE_RETCODE_REJECT_CANCEL: Final[int] = 10041
TRADE_RETCODE_LONG_ONLY: Final[int] = 10042
TRADE_RETCODE_SHORT_ONLY: Final[int] = 10043
TRADE_RETCODE_CLOSE_ONLY: Final[int] = 10044
TRADE_RETCODE_FIFO_CLOSE: Final[int] = 10045

# --- function error codes, last_error() ---
RES_S_OK: Final[int] = 1
RES_E_FAIL: Final[int] = -1
RES_E_INVALID_PARAMS: Final[int] = -2
RES_E_NO_MEMORY: Final[int] = -3
RES_E_NOT_FOUND: Final[int] = -4
RES_E_INVALID_VERSION: Final[int] = -5
RES_E_AUTH_FAILED: Final[int] = -6
RES_E_UNSUPPORTED: Final[int] = -7
RES_E_AUTO_TRADING_DISABLED: Final[int] = -8
RES_E_INTERNAL_FAIL: Final[int] = -10000
RES_E_INTERNAL_FAIL_SEND: Final[int] = -10001
RES_E_INTERNAL_FAIL_RECEIVE: Final[int] = -10002
RES_E_INTERNAL_FAIL_INIT: Final[int] = -10003
RES_E_INTERNAL_FAIL_CONNECT: Final[int] = -10004
RES_E_INTERNAL_FAIL_TIMEOUT: Final[int] = -10005

class TradeRequest(TypedDict,total=False):
    action:int
    magic:int
    order:int
    symbol:str
    volume:float
    price:float
    stoplimit:float
    sl:float    
    tp:float
    deviation:int
    type:int
    type_filling:int
    type_time:int
    expiration:int
    comment:str
    position:int
    position_by:int



class OrderSendResult(NamedTuple):
    retcode: int
    deal: int
    order: int
    volume: float
    price: float
    bid: float
    ask: float
    comment: str
    request_id: int
    retcode_external: int
    request: TradeRequest



class TradePosition(NamedTuple):
    ticket:int
    time:int
    time_msc:int
    time_update:int
    time_update_msc:int
    type:int
    magic:int
    identifier:int
    reason:int
    volume:float
    price_open:float
    sl:float
    tp:float
    price_current:float
    swap:float
    profit:float
    symbol:str
    comment:str
    external_id:str




class Tick(NamedTuple):
    time:int
    bid:float
    ask:float
    last:float
    volume:int
    time_msc:int
    flags:int
    volume_real:float



class TradeOrder(NamedTuple):
    ticket:int
    time_setup:int
    time_setup_msc:int
    time_done:int
    time_done_msc:int
    time_expiration:int
    type:int
    type_time:int
    type_filling:int
    state:int
    magic:int
    position_id:int
    position_by_id:int
    reason:int
    volume_initial:float
    volume_current:float
    price_open:float
    sl:float
    tp:float
    price_current:float
    price_stoplimit:float
    symbol:str
    comment:str
    external_id:str







def initialize(
    path: str = ...,
    *,
    login: int = ...,
    password: str = ...,
    server: str = ...,
    timeout: int = ...,
    portable: bool = ...,
) -> bool: 
    """
    Establish a connection with the MetaTrader 5 terminal.\n

    """
    ...


def shutdown()->None:
    """
    Close the IPC channel between your Python code and the MT5 terminal.\n
    (at the OS process level).
    """
    ...



def order_send(request:TradeRequest)->OrderSendResult|None:
    """
    order is "required for modifying pending orders" (not always),\n
    symbol is "not required when modifying orders and closing positions",\n
    position/position_by are only needed for closing positions,\n
    stoplimit only applies to specific pending order types,\n
    expiration only applies with ORDER_TIME_SPECIFIED.
    """
    ...



def positions_get(
    *,
    symbol :str =...,
    group: str=...,
    ticket: int=...,  
                )->tuple[TradePosition,...] | None:
    """
    Get open positions with the ability to filter by symbol or ticket. There are three call options.\n
    Call without parameters. Return open positions for all symbols.\n
    Call specifying a symbol open positions should be received for.\n
    Call specifying a group of symbols open positions should be received for.\n
    Call specifying a position ticket.
    """
    ...


def symbol_info_tick(
        symbol:str 
                )->Tick |None:
    """
    Get the last tick for the specified financial instrument.\n

    
    """
    ...






def last_error()->tuple[int,str]:
    """Return data on the last error.

    Return value: tuple(code, description), where code is one of the
    RES_* constants above (e.g. RES_S_OK on success, RES_E_FAIL on
    generic failure), and description is a human-readable string.
    """
    ...


def order_calc_margin(action:int,symbol:str,volume:float,price:float,/)->float|None:
    """
    Return margin in the account currency to perform a specified trading operation.
    """
    ...



def orders_get(*, symbol: str = ..., group: str = ..., ticket: int = ...) -> tuple[TradeOrder,...]|None:
    """
    Get active orders with the ability to filter by symbol or ticket.\n
     
    There are three call options.\n
    Call without parameters. Return active orders on all symbols.Call specifying a symbol active orders should be received for.
    Call specifying a group of symbols active orders should be received for.Call specifying the order ticket.
    """
    ...


def copy_rates_from_pos(
   symbol:str,
   timeframe:int ,   # e.g. mt5.TIMEFRAME_H1
   start_pos:int ,   # starting bar index (0 = most recent/current bar)
   count:int ,/        # number of bars to retrieve
)->np.ndarray | None:
    """
    Get bars(candels) from the MetaTrader 5 terminal starting from the specified index.
    
    """
    ...


def positions_total()->int:
    """
    Get the number of open positions.
    """
    ...