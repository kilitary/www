# MetaTrader5 Python API Documentation

## initialize

Establish a connection with the MetaTrader 5 terminal. There are three call options.

**Parameters**

|path|
|----|

path
path
[in] Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. It is indicated first without a parameter name. If the path is not specified, the module attempts to find the executable file on its own.
[in]  Path to the metatrader.exe or metatrader64.exe file. Optional unnamed parameter. It is indicated first without a parameter name. If the path is not specified, the module attempts to find the executable file on its own.
login=LOGIN
login=LOGIN
[in]  Trading account number. Optional named parameter. If not specified, the last trading account is used.
[in]  Trading account number. Optional named parameter. If not specified, the last trading account is used.
password="PASSWORD"
password="PASSWORD"
[in]  Trading account password. Optional named parameter. If the password is not set, the password for a specified trading account saved in the terminal database is applied automatically.
[in]  Trading account password. Optional named parameter. If the password is not set, the password for a specified trading account saved in the terminal database is applied automatically.
server="SERVER"
server="SERVER"
[in]  Trade server name. Optional named parameter. If the server is not set, the server for a specified trading account saved in the terminal database is applied automatically.
[in]  Trade server name. Optional named parameter. If the server is not set, the server for a specified trading account saved in the terminal database is applied automatically.
timeout=TIMEOUT
timeout=TIMEOUT
[in]  Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied.
[in]  Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied.
portable=False
portable=False
[in]  Flag of the terminal launch inportablemode. Optional named parameter. If not specified, the value of False is used.
[in]  Flag of the terminal launch inportablemode. Optional named parameter. If not specified, the value of False is used.

**Return Value**

Returns True in case of successful connection to the MetaTrader 5 terminal, otherwise - False.
Returns True in case of successful connection to the MetaTrader 5 terminal, otherwise - False.

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish MetaTrader 5 connection to a specified trading accountif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish MetaTrader 5 connection to a specified trading accountif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish MetaTrader 5 connection to a specified trading accountif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish MetaTrader 5 connection to a specified trading accountif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish MetaTrader 5 connection to a specified trading account
if not
mt5.initialize
(login=25115284, server=
"MetaQuotes-Demo"
,password=
"4zatlbqx"
):
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# display data on connection status, server name and trading account
print
(
mt5
.
terminal_info
())
# display data on MetaTrader 5 version
print
(
mt5
.
version
())
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()

---

## shutdown

Close the previously established connection to the MetaTrader 5 terminal.

**Return Value**

None.
None.
Example:
Example:
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed"
)
quit
()
# display data on connection status, server name and trading account
print
(
mt5
.
terminal_info
())
# display data on MetaTrader 5 version
print
(
mt5
.
version
())
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed")quit()# display data on connection status, server name and trading accountprint(mt5.terminal_info())# display data on MetaTrader 5 versionprint(mt5.version())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed"
)
quit
()
# display data on connection status, server name and trading account
print
(
mt5
.
terminal_info
())
# display data on MetaTrader 5 version
print
(
mt5
.
version
())
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()

---

## version

Return the MetaTrader 5 terminal version.

**Return Value**

Return the MetaTrader 5 terminal version, build and release date. Return None in case of an error. The info on the error can be obtained usinglast_error().
Return the MetaTrader 5 terminal version, build and release date. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display data on connection status, server name and trading account 'as is'print(mt5.terminal_info())print()# get properties in the form of a dictionaryterminal_info_dict=mt5.terminal_info()._asdict()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df[:-1])# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2367, '23 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...terminal_info() as dataframe:property                         value0       community_account                          True1    community_connection                          True2               connected                          True3            dlls_allowed                         False4           trade_allowed                         False5       tradeapi_disabled                         False6           email_enabled                         False7             ftp_enabled                         False8   notifications_enabled                         False9                    mqid                         False10                  build                          236711                maxbars                          500012               codepage                          125113              ping_last                         7788114      community_balance                       707.10715         retransmission                             016                company     MetaQuotes Software Corp.17                   name                  MetaTrader 518               language                       Russian19                   path  E:\ProgramFiles\MetaTrader 520              data_path  E:\ProgramFiles\MetaTrader 5
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display data on connection status, server name and trading account 'as is'print(mt5.terminal_info())print()# get properties in the form of a dictionaryterminal_info_dict=mt5.terminal_info()._asdict()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df[:-1])# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2367, '23 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...terminal_info() as dataframe:property                         value0       community_account                          True1    community_connection                          True2               connected                          True3            dlls_allowed                         False4           trade_allowed                         False5       tradeapi_disabled                         False6           email_enabled                         False7             ftp_enabled                         False8   notifications_enabled                         False9                    mqid                         False10                  build                          236711                maxbars                          500012               codepage                          125113              ping_last                         7788114      community_balance                       707.10715         retransmission                             016                company     MetaQuotes Software Corp.17                   name                  MetaTrader 518               language                       Russian19                   path  E:\ProgramFiles\MetaTrader 520              data_path  E:\ProgramFiles\MetaTrader 5
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display data on connection status, server name and trading account 'as is'print(mt5.terminal_info())print()# get properties in the form of a dictionaryterminal_info_dict=mt5.terminal_info()._asdict()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df[:-1])# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2367, '23 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...terminal_info() as dataframe:property                         value0       community_account                          True1    community_connection                          True2               connected                          True3            dlls_allowed                         False4           trade_allowed                         False5       tradeapi_disabled                         False6           email_enabled                         False7             ftp_enabled                         False8   notifications_enabled                         False9                    mqid                         False10                  build                          236711                maxbars                          500012               codepage                          125113              ping_last                         7788114      community_balance                       707.10715         retransmission                             016                company     MetaQuotes Software Corp.17                   name                  MetaTrader 518               language                       Russian19                   path  E:\ProgramFiles\MetaTrader 520              data_path  E:\ProgramFiles\MetaTrader 5
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display data on connection status, server name and trading account 'as is'print(mt5.terminal_info())print()# get properties in the form of a dictionaryterminal_info_dict=mt5.terminal_info()._asdict()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df[:-1])# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2367, '23 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...terminal_info() as dataframe:property                         value0       community_account                          True1    community_connection                          True2               connected                          True3            dlls_allowed                         False4           trade_allowed                         False5       tradeapi_disabled                         False6           email_enabled                         False7             ftp_enabled                         False8   notifications_enabled                         False9                    mqid                         False10                  build                          236711                maxbars                          500012               codepage                          125113              ping_last                         7788114      community_balance                       707.10715         retransmission                             016                company     MetaQuotes Software Corp.17                   name                  MetaTrader 518               language                       Russian19                   path  E:\ProgramFiles\MetaTrader 520              data_path  E:\ProgramFiles\MetaTrader 5
import
MetaTrader5
as
mt5
import
pandas
as
pd
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# display data on MetaTrader 5 version
print
(
mt5.version
())
# display data on connection status, server name and trading account 'as is'
print
(
mt5.terminal_info
())
print
()
# get properties in the form of a dictionary
terminal_info_dict=
mt5.terminal_info()._asdict()
# convert the dictionary into DataFrame and print
df=
pd.DataFrame
(
list
(terminal_info_dict.items()),columns=['property','value'])
print
(
"terminal_info() as dataframe:"
)
print
(df[:-1])
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
[500, 2367, '23 Mar 2020']
TerminalInfo(community_account=True, community_connection=True, connected=True, dlls_allowed=False, trade_allowed=False, ...
terminal_info() as dataframe:
property                         value
0       community_account                          True
1    community_connection                          True
2               connected                          True
3            dlls_allowed                         False
4           trade_allowed                         False
5       tradeapi_disabled                         False
6           email_enabled                         False
7             ftp_enabled                         False
8   notifications_enabled                         False
9                    mqid                         False
10                  build                          2367
11                maxbars                          5000
12               codepage                          1251
13              ping_last                         77881
14      community_balance                       707.107
15         retransmission                             0
16                company     MetaQuotes Software Corp.
17                   name                  MetaTrader 5
18               language                       Russian
19                   path  E:\ProgramFiles\MetaTrader 5
20              data_path  E:\ProgramFiles\MetaTrader 5

---

## last_error

Return data on the last error.

**Return Value**

Return the last error code and description as a tuple.
Return the last error code and description as a tuple.

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## account_info

Get info on the current trading account.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# connect to the trade account specifying a password and a serverauthorized=mt5.login(25115284,password="gqz0343lbdm")ifauthorized:account_info=mt5.account_info()ifaccount_info!=None:# display trading account data 'as is'print(account_info)# display trading account data in the form of a dictionaryprint("Show account_info()._asdict():")account_info_dict =mt5.account_info()._asdict()forpropinaccount_info_dict:print("  {}={}".format(prop, account_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])print("account_info() as dataframe:")print(df)else:print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....Show account_info()._asdict():login=25115284trade_mode=0leverage=100limit_orders=200margin_so_mode=0trade_allowed=Truetrade_expert=Truemargin_mode=2currency_digits=2fifo_close=Falsebalance=99511.4credit=0.0profit=41.82equity=99553.22margin=98.18margin_free=99455.04margin_level=101398.67590140559margin_so_call=50.0margin_so_so=30.0margin_initial=0.0margin_maintenance=0.0assets=0.0liabilities=0.0commission_blocked=0.0server=MetaQuotes-Democurrency=USDcompany=MetaQuotes Software Corp.account_info() as dataframeproperty                      value0                login                   251152841           trade_mode                          02             leverage                        1003         limit_orders                        2004       margin_so_mode                          05        trade_allowed                       True6         trade_expert                       True7          margin_mode                          28      currency_digits                          29           fifo_close                      False10             balance                    99588.311              credit                          012              profit                     -45.1313              equity                    99543.214              margin                      54.3715         margin_free                    99488.816        margin_level                     18308517      margin_so_call                         5018        margin_so_so                         3019      margin_initial                          020  margin_maintenance                          021              assets                          022         liabilities                          023  commission_blocked                          024                name                James Smith25              server            MetaQuotes-Demo26            currency                        USD27             company  MetaQuotes Software Corp.
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# connect to the trade account specifying a password and a serverauthorized=mt5.login(25115284,password="gqz0343lbdm")ifauthorized:account_info=mt5.account_info()ifaccount_info!=None:# display trading account data 'as is'print(account_info)# display trading account data in the form of a dictionaryprint("Show account_info()._asdict():")account_info_dict =mt5.account_info()._asdict()forpropinaccount_info_dict:print("  {}={}".format(prop, account_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])print("account_info() as dataframe:")print(df)else:print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....Show account_info()._asdict():login=25115284trade_mode=0leverage=100limit_orders=200margin_so_mode=0trade_allowed=Truetrade_expert=Truemargin_mode=2currency_digits=2fifo_close=Falsebalance=99511.4credit=0.0profit=41.82equity=99553.22margin=98.18margin_free=99455.04margin_level=101398.67590140559margin_so_call=50.0margin_so_so=30.0margin_initial=0.0margin_maintenance=0.0assets=0.0liabilities=0.0commission_blocked=0.0server=MetaQuotes-Democurrency=USDcompany=MetaQuotes Software Corp.account_info() as dataframeproperty                      value0                login                   251152841           trade_mode                          02             leverage                        1003         limit_orders                        2004       margin_so_mode                          05        trade_allowed                       True6         trade_expert                       True7          margin_mode                          28      currency_digits                          29           fifo_close                      False10             balance                    99588.311              credit                          012              profit                     -45.1313              equity                    99543.214              margin                      54.3715         margin_free                    99488.816        margin_level                     18308517      margin_so_call                         5018        margin_so_so                         3019      margin_initial                          020  margin_maintenance                          021              assets                          022         liabilities                          023  commission_blocked                          024                name                James Smith25              server            MetaQuotes-Demo26            currency                        USD27             company  MetaQuotes Software Corp.
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# connect to the trade account specifying a password and a serverauthorized=mt5.login(25115284,password="gqz0343lbdm")ifauthorized:account_info=mt5.account_info()ifaccount_info!=None:# display trading account data 'as is'print(account_info)# display trading account data in the form of a dictionaryprint("Show account_info()._asdict():")account_info_dict =mt5.account_info()._asdict()forpropinaccount_info_dict:print("  {}={}".format(prop, account_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])print("account_info() as dataframe:")print(df)else:print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....Show account_info()._asdict():login=25115284trade_mode=0leverage=100limit_orders=200margin_so_mode=0trade_allowed=Truetrade_expert=Truemargin_mode=2currency_digits=2fifo_close=Falsebalance=99511.4credit=0.0profit=41.82equity=99553.22margin=98.18margin_free=99455.04margin_level=101398.67590140559margin_so_call=50.0margin_so_so=30.0margin_initial=0.0margin_maintenance=0.0assets=0.0liabilities=0.0commission_blocked=0.0server=MetaQuotes-Democurrency=USDcompany=MetaQuotes Software Corp.account_info() as dataframeproperty                      value0                login                   251152841           trade_mode                          02             leverage                        1003         limit_orders                        2004       margin_so_mode                          05        trade_allowed                       True6         trade_expert                       True7          margin_mode                          28      currency_digits                          29           fifo_close                      False10             balance                    99588.311              credit                          012              profit                     -45.1313              equity                    99543.214              margin                      54.3715         margin_free                    99488.816        margin_level                     18308517      margin_so_call                         5018        margin_so_so                         3019      margin_initial                          020  margin_maintenance                          021              assets                          022         liabilities                          023  commission_blocked                          024                name                James Smith25              server            MetaQuotes-Demo26            currency                        USD27             company  MetaQuotes Software Corp.
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# connect to the trade account specifying a password and a serverauthorized=mt5.login(25115284,password="gqz0343lbdm")ifauthorized:account_info=mt5.account_info()ifaccount_info!=None:# display trading account data 'as is'print(account_info)# display trading account data in the form of a dictionaryprint("Show account_info()._asdict():")account_info_dict =mt5.account_info()._asdict()forpropinaccount_info_dict:print("  {}={}".format(prop, account_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])print("account_info() as dataframe:")print(df)else:print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....Show account_info()._asdict():login=25115284trade_mode=0leverage=100limit_orders=200margin_so_mode=0trade_allowed=Truetrade_expert=Truemargin_mode=2currency_digits=2fifo_close=Falsebalance=99511.4credit=0.0profit=41.82equity=99553.22margin=98.18margin_free=99455.04margin_level=101398.67590140559margin_so_call=50.0margin_so_so=30.0margin_initial=0.0margin_maintenance=0.0assets=0.0liabilities=0.0commission_blocked=0.0server=MetaQuotes-Democurrency=USDcompany=MetaQuotes Software Corp.account_info() as dataframeproperty                      value0                login                   251152841           trade_mode                          02             leverage                        1003         limit_orders                        2004       margin_so_mode                          05        trade_allowed                       True6         trade_expert                       True7          margin_mode                          28      currency_digits                          29           fifo_close                      False10             balance                    99588.311              credit                          012              profit                     -45.1313              equity                    99543.214              margin                      54.3715         margin_free                    99488.816        margin_level                     18308517      margin_so_call                         5018        margin_so_so                         3019      margin_initial                          020  margin_maintenance                          021              assets                          022         liabilities                          023  commission_blocked                          024                name                James Smith25              server            MetaQuotes-Demo26            currency                        USD27             company  MetaQuotes Software Corp.
import
MetaTrader5
as
mt5
import
pandas
as
pd
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# connect to the trade account specifying a password and a server
authorized
=
mt5.login
(
25115284
,
password
=
"gqz0343lbdm"
)
if
authorized
:
account_info=
mt5.account_info
()
if
account_info!
=
None
:
# display trading account data 'as is'
print
(
account_info
)
# display trading account data in the form of a dictionary
print
(
"Show account_info()._asdict():"
)
account_info_dict =
mt5.account_info()._asdict
()
for
prop
in
account_info_dict:
print
(
"  {}={}"
.
format
(prop, account_info_dict[prop]))
print
()
# convert the dictionary into DataFrame and print
df
=pd.DataFrame
(
list
(account_info_dict.items()),columns=['property','value'])
print
(
"account_info() as dataframe:"
)
print
(df)
else
:
print
(
"failed to connect to trade account 25115284 with password=gqz0343lbdm, error code ="
,
mt5.last_error()
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200, margin_so_mode=0, ....
Show account_info()._asdict():
login=25115284
trade_mode=0
leverage=100
limit_orders=200
margin_so_mode=0
trade_allowed=True
trade_expert=True
margin_mode=2
currency_digits=2
fifo_close=False
balance=99511.4
credit=0.0
profit=41.82
equity=99553.22
margin=98.18
margin_free=99455.04
margin_level=101398.67590140559
margin_so_call=50.0
margin_so_so=30.0
margin_initial=0.0
margin_maintenance=0.0
assets=0.0
liabilities=0.0
commission_blocked=0.0
server=MetaQuotes-Demo
currency=USD
company=MetaQuotes Software Corp.
account_info() as dataframe
property                      value
0                login                   25115284
1           trade_mode                          0
2             leverage                        100
3         limit_orders                        200
4       margin_so_mode                          0
5        trade_allowed                       True
6         trade_expert                       True
7          margin_mode                          2
8      currency_digits                          2
9           fifo_close                      False
10             balance                    99588.3
11              credit                          0
12              profit                     -45.13
13              equity                    99543.2
14              margin                      54.37
15         margin_free                    99488.8
16        margin_level                     183085
17      margin_so_call                         50
18        margin_so_so                         30
19      margin_initial                          0
20  margin_maintenance                          0
21              assets                          0
22         liabilities                          0
23  commission_blocked                          0
24                name                James Smith
25              server            MetaQuotes-Demo
26            currency                        USD
27             company  MetaQuotes Software Corp.

---

## terminal_info

Get the connected MetaTrader 5 client terminal status and settings.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display info on the terminal settings and statusterminal_info=mt5.terminal_info()ifterminal_info!=None:# display the terminal data 'as is'print(terminal_info)# display data in the form of a listprint("Show terminal_info()._asdict():")terminal_info_dict =mt5.terminal_info()._asdict()forpropinterminal_info_dict:print("  {}={}".format(prop, terminal_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2366, '20 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True,....Show terminal_info()._asdict():community_account=Truecommunity_connection=Trueconnected=Truedlls_allowed=Falsetrade_allowed=Falsetradeapi_disabled=Falseemail_enabled=Falseftp_enabled=Falsenotifications_enabled=Falsemqid=Falsebuild=2366maxbars=5000codepage=1251ping_last=77850community_balance=707.10668201585retransmission=0.0company=MetaQuotes Software Corp.name=MetaTrader 5language=Russianpath=E:\ProgramFiles\MetaTrader 5data_path=E:\ProgramFiles\MetaTrader 5commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Commonterminal_info() as dataframe:property                      value0       community_account                       True1    community_connection                       True2               connected                       True3            dlls_allowed                      False4           trade_allowed                      False5       tradeapi_disabled                      False6           email_enabled                      False7             ftp_enabled                      False8   notifications_enabled                      False9                    mqid                      False10                  build                       236711                maxbars                       500012               codepage                       125113              ping_last                      8095314      community_balance                    707.10715         retransmission                   0.06359316                company  MetaQuotes Software Corp.17                   name               MetaTrader 518               language                    Russian
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display info on the terminal settings and statusterminal_info=mt5.terminal_info()ifterminal_info!=None:# display the terminal data 'as is'print(terminal_info)# display data in the form of a listprint("Show terminal_info()._asdict():")terminal_info_dict =mt5.terminal_info()._asdict()forpropinterminal_info_dict:print("  {}={}".format(prop, terminal_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2366, '20 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True,....Show terminal_info()._asdict():community_account=Truecommunity_connection=Trueconnected=Truedlls_allowed=Falsetrade_allowed=Falsetradeapi_disabled=Falseemail_enabled=Falseftp_enabled=Falsenotifications_enabled=Falsemqid=Falsebuild=2366maxbars=5000codepage=1251ping_last=77850community_balance=707.10668201585retransmission=0.0company=MetaQuotes Software Corp.name=MetaTrader 5language=Russianpath=E:\ProgramFiles\MetaTrader 5data_path=E:\ProgramFiles\MetaTrader 5commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Commonterminal_info() as dataframe:property                      value0       community_account                       True1    community_connection                       True2               connected                       True3            dlls_allowed                      False4           trade_allowed                      False5       tradeapi_disabled                      False6           email_enabled                      False7             ftp_enabled                      False8   notifications_enabled                      False9                    mqid                      False10                  build                       236711                maxbars                       500012               codepage                       125113              ping_last                      8095314      community_balance                    707.10715         retransmission                   0.06359316                company  MetaQuotes Software Corp.17                   name               MetaTrader 518               language                    Russian
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display info on the terminal settings and statusterminal_info=mt5.terminal_info()ifterminal_info!=None:# display the terminal data 'as is'print(terminal_info)# display data in the form of a listprint("Show terminal_info()._asdict():")terminal_info_dict =mt5.terminal_info()._asdict()forpropinterminal_info_dict:print("  {}={}".format(prop, terminal_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2366, '20 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True,....Show terminal_info()._asdict():community_account=Truecommunity_connection=Trueconnected=Truedlls_allowed=Falsetrade_allowed=Falsetradeapi_disabled=Falseemail_enabled=Falseftp_enabled=Falsenotifications_enabled=Falsemqid=Falsebuild=2366maxbars=5000codepage=1251ping_last=77850community_balance=707.10668201585retransmission=0.0company=MetaQuotes Software Corp.name=MetaTrader 5language=Russianpath=E:\ProgramFiles\MetaTrader 5data_path=E:\ProgramFiles\MetaTrader 5commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Commonterminal_info() as dataframe:property                      value0       community_account                       True1    community_connection                       True2               connected                       True3            dlls_allowed                      False4           trade_allowed                      False5       tradeapi_disabled                      False6           email_enabled                      False7             ftp_enabled                      False8   notifications_enabled                      False9                    mqid                      False10                  build                       236711                maxbars                       500012               codepage                       125113              ping_last                      8095314      community_balance                    707.10715         retransmission                   0.06359316                company  MetaQuotes Software Corp.17                   name               MetaTrader 518               language                    Russian
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on MetaTrader 5 versionprint(mt5.version())# display info on the terminal settings and statusterminal_info=mt5.terminal_info()ifterminal_info!=None:# display the terminal data 'as is'print(terminal_info)# display data in the form of a listprint("Show terminal_info()._asdict():")terminal_info_dict =mt5.terminal_info()._asdict()forpropinterminal_info_dict:print("  {}={}".format(prop, terminal_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])print("terminal_info() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29[500, 2366, '20 Mar 2020']TerminalInfo(community_account=True, community_connection=True, connected=True,....Show terminal_info()._asdict():community_account=Truecommunity_connection=Trueconnected=Truedlls_allowed=Falsetrade_allowed=Falsetradeapi_disabled=Falseemail_enabled=Falseftp_enabled=Falsenotifications_enabled=Falsemqid=Falsebuild=2366maxbars=5000codepage=1251ping_last=77850community_balance=707.10668201585retransmission=0.0company=MetaQuotes Software Corp.name=MetaTrader 5language=Russianpath=E:\ProgramFiles\MetaTrader 5data_path=E:\ProgramFiles\MetaTrader 5commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Commonterminal_info() as dataframe:property                      value0       community_account                       True1    community_connection                       True2               connected                       True3            dlls_allowed                      False4           trade_allowed                      False5       tradeapi_disabled                      False6           email_enabled                      False7             ftp_enabled                      False8   notifications_enabled                      False9                    mqid                      False10                  build                       236711                maxbars                       500012               codepage                       125113              ping_last                      8095314      community_balance                    707.10715         retransmission                   0.06359316                company  MetaQuotes Software Corp.17                   name               MetaTrader 518               language                    Russian
import
MetaTrader5
as
mt5
import
pandas
as
pd
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# display data on MetaTrader 5 version
print
(
mt5.version
())
# display info on the terminal settings and status
terminal_info=
mt5.terminal_info
()
if
terminal_info!
=
None
:
# display the terminal data 'as is'
print
(
terminal_info
)
# display data in the form of a list
print
(
"Show terminal_info()._asdict():"
)
terminal_info_dict =
mt5.terminal_info()._asdict()
for
prop
in
terminal_info_dict:
print
(
"  {}={}"
.format(prop, terminal_info_dict[prop]))
print
()
# convert the dictionary into DataFrame and print
df
=pd.DataFrame
(
list
(terminal_info_dict.items()),columns=['property','value'])
print
(
"terminal_info() as dataframe:"
)
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
[500, 2366, '20 Mar 2020']
TerminalInfo(community_account=True, community_connection=True, connected=True,....
Show terminal_info()._asdict():
community_account=True
community_connection=True
connected=True
dlls_allowed=False
trade_allowed=False
tradeapi_disabled=False
email_enabled=False
ftp_enabled=False
notifications_enabled=False
mqid=False
build=2366
maxbars=5000
codepage=1251
ping_last=77850
community_balance=707.10668201585
retransmission=0.0
company=MetaQuotes Software Corp.
name=MetaTrader 5
language=Russian
path=E:\ProgramFiles\MetaTrader 5
data_path=E:\ProgramFiles\MetaTrader 5
commondata_path=C:\Users\Rosh\AppData\Roaming\MetaQuotes\Terminal\Common
terminal_info() as dataframe:
property                      value
0       community_account                       True
1    community_connection                       True
2               connected                       True
3            dlls_allowed                      False
4           trade_allowed                      False
5       tradeapi_disabled                      False
6           email_enabled                      False
7             ftp_enabled                      False
8   notifications_enabled                      False
9                    mqid                      False
10                  build                       2367
11                maxbars                       5000
12               codepage                       1251
13              ping_last                      80953
14      community_balance                    707.107
15         retransmission                   0.063593
16                company  MetaQuotes Software Corp.
17                   name               MetaTrader 5
18               language                    Russian

---

## symbols_total

Get the number of all financial instruments in the MetaTrader 5 terminal.

**Return Value**

Integer value.
Integer value.

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of financial instrumentssymbols=mt5.symbols_total()ifsymbols>0:print("Total symbols =",symbols)else:print("symbols not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of financial instrumentssymbols=mt5.symbols_total()ifsymbols>0:print("Total symbols =",symbols)else:print("symbols not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of financial instrumentssymbols=mt5.symbols_total()ifsymbols>0:print("Total symbols =",symbols)else:print("symbols not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of financial instrumentssymbols=mt5.symbols_total()ifsymbols>0:print("Total symbols =",symbols)else:print("symbols not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get the number of financial instruments
symbols
=
mt5.symbols_total
()
if
symbols>0
:
print
(
"Total symbols =",
symbols
)
else
:
print
(
"symbols not found"
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## symbols_get

Get all financial instruments from the MetaTrader 5 terminal.

**Return Value**

Return symbols in the form of a tuple. Return None in case of an error. The info on the error can be obtained usinglast_error().
Return symbols in the form of a tuple. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get all symbolssymbols=mt5.symbols_get()print('Symbols: ',len(symbols))count=0# display the first five onesforsinsymbols:count+=1print("{}. {}".format(count,s.name))ifcount==5:breakprint()# get symbols containing RU in their namesru_symbols=mt5.symbols_get("*RU*")print('len(*RU*): ',len(ru_symbols))forsinru_symbols:print(s.name)print()# get symbols whose names do not contain USD, EUR, JPY and GBPgroup_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):',len(group_symbols))forsingroup_symbols:print(s.name,":",s)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Symbols:  841. EURUSD2. GBPUSD3. USDCHF4. USDJPY5. USDCNHlen(*RU*):  8EURUSDUSDRUBUSDRUREURRUREURRUBFORTS.RUB.M5EURUSD_T20EURUSD4len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get all symbolssymbols=mt5.symbols_get()print('Symbols: ',len(symbols))count=0# display the first five onesforsinsymbols:count+=1print("{}. {}".format(count,s.name))ifcount==5:breakprint()# get symbols containing RU in their namesru_symbols=mt5.symbols_get("*RU*")print('len(*RU*): ',len(ru_symbols))forsinru_symbols:print(s.name)print()# get symbols whose names do not contain USD, EUR, JPY and GBPgroup_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):',len(group_symbols))forsingroup_symbols:print(s.name,":",s)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Symbols:  841. EURUSD2. GBPUSD3. USDCHF4. USDJPY5. USDCNHlen(*RU*):  8EURUSDUSDRUBUSDRUREURRUREURRUBFORTS.RUB.M5EURUSD_T20EURUSD4len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get all symbolssymbols=mt5.symbols_get()print('Symbols: ',len(symbols))count=0# display the first five onesforsinsymbols:count+=1print("{}. {}".format(count,s.name))ifcount==5:breakprint()# get symbols containing RU in their namesru_symbols=mt5.symbols_get("*RU*")print('len(*RU*): ',len(ru_symbols))forsinru_symbols:print(s.name)print()# get symbols whose names do not contain USD, EUR, JPY and GBPgroup_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):',len(group_symbols))forsingroup_symbols:print(s.name,":",s)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Symbols:  841. EURUSD2. GBPUSD3. USDCHF4. USDJPY5. USDCNHlen(*RU*):  8EURUSDUSDRUBUSDRUREURRUREURRUBFORTS.RUB.M5EURUSD_T20EURUSD4len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get all symbolssymbols=mt5.symbols_get()print('Symbols: ',len(symbols))count=0# display the first five onesforsinsymbols:count+=1print("{}. {}".format(count,s.name))ifcount==5:breakprint()# get symbols containing RU in their namesru_symbols=mt5.symbols_get("*RU*")print('len(*RU*): ',len(ru_symbols))forsinru_symbols:print(s.name)print()# get symbols whose names do not contain USD, EUR, JPY and GBPgroup_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):',len(group_symbols))forsingroup_symbols:print(s.name,":",s)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Symbols:  841. EURUSD2. GBPUSD3. USDCHF4. USDJPY5. USDCNHlen(*RU*):  8EURUSDUSDRUBUSDRUREURRUREURRUBFORTS.RUB.M5EURUSD_T20EURUSD4len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get all symbols
symbols=
mt5.symbols_get()
print
(
'Symbols: '
,
len
(symbols))
count=0
# display the first five ones
for
s
in
symbols:
count+=1
print
(
"{}. {}
".
format
(count,s.name))
if
count==5:
break
print
()
# get symbols containing RU in their names
ru_symbols=
mt5.symbols_get
(
"*RU*"
)
print
(
'len(*RU*): '
,
len
(ru_symbols))
for
s
in
ru_symbols:
print
(s.name)
print
()
# get symbols whose names do not contain USD, EUR, JPY and GBP
group_symbols=
mt5.symbols_get
(group=
"*,!*USD*,!*EUR*,!*JPY*,!*GBP*"
)
print
(
'len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):'
,
len
(group_symbols))
for
s
in
group_symbols:
print
(s.name,
":"
,s)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Symbols:  84
1. EURUSD
2. GBPUSD
3. USDCHF
4. USDJPY
5. USDCNH
len(*RU*):  8
EURUSD
USDRUB
USDRUR
EURRUR
EURRUB
FORTS.RUB.M5
EURUSD_T20
EURUSD4
len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13
AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session...
AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, sessi...
FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...
FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False, visible=False, session_deals=0, session_buy_orders=0, ...

---

## symbol_info

Get data on the specified financial instrument.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURJPY symbol in MarketWatchselected=mt5.symbol_select("EURJPY",True)if notselected:print("Failed to select EURJPY")mt5.shutdown()quit()# display EURJPY symbol propertiessymbol_info=mt5.symbol_info("EURJPY")ifsymbol_info!=None:# display the terminal data 'as is'print(symbol_info)print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)# display symbol properties as a listprint("Show symbol_info(\"EURJPY\")._asdict():")symbol_info_dict =mt5.symbol_info("EURJPY")._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...EURJPY: spread = 17   digits = 3Show symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585069682digits=3spread=17spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=120.024bidhigh=120.506bidlow=118.798ask=120.041askhigh=120.526asklow=118.828last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=0.001trade_tick_value=0.8977708350166538trade_tick_value_profit=0.8977708350166538trade_tick_value_loss=0.8978272580355541trade_tick_size=0.001trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-0.2swap_short=-1.2margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=JPYcurrency_margin=EURbank=description=Euro vs Japanese Yenexchange=formula=isin=name=EURJPYpage=http://www.google.com/finance?q=EURJPYpath=Forex\EURJPY
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURJPY symbol in MarketWatchselected=mt5.symbol_select("EURJPY",True)if notselected:print("Failed to select EURJPY")mt5.shutdown()quit()# display EURJPY symbol propertiessymbol_info=mt5.symbol_info("EURJPY")ifsymbol_info!=None:# display the terminal data 'as is'print(symbol_info)print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)# display symbol properties as a listprint("Show symbol_info(\"EURJPY\")._asdict():")symbol_info_dict =mt5.symbol_info("EURJPY")._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...EURJPY: spread = 17   digits = 3Show symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585069682digits=3spread=17spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=120.024bidhigh=120.506bidlow=118.798ask=120.041askhigh=120.526asklow=118.828last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=0.001trade_tick_value=0.8977708350166538trade_tick_value_profit=0.8977708350166538trade_tick_value_loss=0.8978272580355541trade_tick_size=0.001trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-0.2swap_short=-1.2margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=JPYcurrency_margin=EURbank=description=Euro vs Japanese Yenexchange=formula=isin=name=EURJPYpage=http://www.google.com/finance?q=EURJPYpath=Forex\EURJPY
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURJPY symbol in MarketWatchselected=mt5.symbol_select("EURJPY",True)if notselected:print("Failed to select EURJPY")mt5.shutdown()quit()# display EURJPY symbol propertiessymbol_info=mt5.symbol_info("EURJPY")ifsymbol_info!=None:# display the terminal data 'as is'print(symbol_info)print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)# display symbol properties as a listprint("Show symbol_info(\"EURJPY\")._asdict():")symbol_info_dict =mt5.symbol_info("EURJPY")._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...EURJPY: spread = 17   digits = 3Show symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585069682digits=3spread=17spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=120.024bidhigh=120.506bidlow=118.798ask=120.041askhigh=120.526asklow=118.828last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=0.001trade_tick_value=0.8977708350166538trade_tick_value_profit=0.8977708350166538trade_tick_value_loss=0.8978272580355541trade_tick_size=0.001trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-0.2swap_short=-1.2margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=JPYcurrency_margin=EURbank=description=Euro vs Japanese Yenexchange=formula=isin=name=EURJPYpage=http://www.google.com/finance?q=EURJPYpath=Forex\EURJPY
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURJPY symbol in MarketWatchselected=mt5.symbol_select("EURJPY",True)if notselected:print("Failed to select EURJPY")mt5.shutdown()quit()# display EURJPY symbol propertiessymbol_info=mt5.symbol_info("EURJPY")ifsymbol_info!=None:# display the terminal data 'as is'print(symbol_info)print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)# display symbol properties as a listprint("Show symbol_info(\"EURJPY\")._asdict():")symbol_info_dict =mt5.symbol_info("EURJPY")._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...EURJPY: spread = 17   digits = 3Show symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585069682digits=3spread=17spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=120.024bidhigh=120.506bidlow=118.798ask=120.041askhigh=120.526asklow=118.828last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=0.001trade_tick_value=0.8977708350166538trade_tick_value_profit=0.8977708350166538trade_tick_value_loss=0.8978272580355541trade_tick_size=0.001trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-0.2swap_short=-1.2margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=JPYcurrency_margin=EURbank=description=Euro vs Japanese Yenexchange=formula=isin=name=EURJPYpage=http://www.google.com/finance?q=EURJPYpath=Forex\EURJPY
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# attempt to enable the display of the EURJPY symbol in MarketWatch
selected
=
mt5.symbol_select
(
"EURJPY"
,
True
)
if not
selected
:
print
(
"Failed to select EURJPY"
)
mt5
.
shutdown
()
quit
()
# display EURJPY symbol properties
symbol_info
=
mt5.symbol_info
(
"EURJPY"
)
if
symbol_info!
=
None
:
# display the terminal data 'as is'
print
(
symbol_info
)
print
(
"EURJPY: spread =",
symbol_info.spread,
"  digits ="
,symbol_info.digits
)
# display symbol properties as a list
print
(
"Show symbol_info(\"EURJPY\")._asdict():"
)
symbol_info_dict =
mt5.symbol_info
(
"EURJPY"
)
._asdict
()
for
prop
in
symbol_info_dict:
print
(
"  {}={}"
.format(prop, symbol_info_dict[prop]))
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, ...
EURJPY: spread = 17   digits = 3
Show symbol_info()._asdict():
custom=False
chart_mode=0
select=True
visible=True
session_deals=0
session_buy_orders=0
session_sell_orders=0
volume=0
volumehigh=0
volumelow=0
time=1585069682
digits=3
spread=17
spread_float=True
ticks_bookdepth=10
trade_calc_mode=0
trade_mode=4
start_time=0
expiration_time=0
trade_stops_level=0
trade_freeze_level=0
trade_exemode=1
swap_mode=1
swap_rollover3days=3
margin_hedged_use_leg=False
expiration_mode=7
filling_mode=1
order_mode=127
order_gtc_mode=0
option_mode=0
option_right=0
bid=120.024
bidhigh=120.506
bidlow=118.798
ask=120.041
askhigh=120.526
asklow=118.828
last=0.0
lasthigh=0.0
lastlow=0.0
volume_real=0.0
volumehigh_real=0.0
volumelow_real=0.0
option_strike=0.0
point=0.001
trade_tick_value=0.8977708350166538
trade_tick_value_profit=0.8977708350166538
trade_tick_value_loss=0.8978272580355541
trade_tick_size=0.001
trade_contract_size=100000.0
trade_accrued_interest=0.0
trade_face_value=0.0
trade_liquidity_rate=0.0
volume_min=0.01
volume_max=500.0
volume_step=0.01
volume_limit=0.0
swap_long=-0.2
swap_short=-1.2
margin_initial=0.0
margin_maintenance=0.0
session_volume=0.0
session_turnover=0.0
session_interest=0.0
session_buy_orders_volume=0.0
session_sell_orders_volume=0.0
session_open=0.0
session_close=0.0
session_aw=0.0
session_price_settlement=0.0
session_price_limit_min=0.0
session_price_limit_max=0.0
margin_hedged=100000.0
price_change=0.0
price_volatility=0.0
price_theoretical=0.0
price_greeks_delta=0.0
price_greeks_theta=0.0
price_greeks_gamma=0.0
price_greeks_vega=0.0
price_greeks_rho=0.0
price_greeks_omega=0.0
price_sensitivity=0.0
basis=
category=
currency_base=EUR
currency_profit=JPY
currency_margin=EUR
bank=
description=Euro vs Japanese Yen
exchange=
formula=
isin=
name=EURJPY
page=http://www.google.com/finance?q=EURJPY
path=Forex\EURJPY

---

## symbol_info_tick

Get the last tick for the specified financial instrument.

**Return Value**

Return info in the form of a tuple. Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a tuple. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the GBPUSD in MarketWatchselected=mt5.symbol_select("GBPUSD",True)if notselected:print("Failed to select GBPUSD")mt5.shutdown()quit()# display the last GBPUSD ticklasttick=mt5.symbol_info_tick("GBPUSD")print(lasttick)# display tick field values in the form of a listprint("Show symbol_info_tick(\"GBPUSD\")._asdict():")symbol_info_tick_dict =mt5.symbol_info_tick("GBPUSD")._asdict()forpropinsymbol_info_tick_dict:print("  {}={}".format(prop, symbol_info_tick_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)Show symbol_info_tick._asdict():time=1585070338bid=1.17264ask=1.17279last=0.0volume=0time_msc=1585070338728flags=2volume_real=0.0
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the GBPUSD in MarketWatchselected=mt5.symbol_select("GBPUSD",True)if notselected:print("Failed to select GBPUSD")mt5.shutdown()quit()# display the last GBPUSD ticklasttick=mt5.symbol_info_tick("GBPUSD")print(lasttick)# display tick field values in the form of a listprint("Show symbol_info_tick(\"GBPUSD\")._asdict():")symbol_info_tick_dict =mt5.symbol_info_tick("GBPUSD")._asdict()forpropinsymbol_info_tick_dict:print("  {}={}".format(prop, symbol_info_tick_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)Show symbol_info_tick._asdict():time=1585070338bid=1.17264ask=1.17279last=0.0volume=0time_msc=1585070338728flags=2volume_real=0.0
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the GBPUSD in MarketWatchselected=mt5.symbol_select("GBPUSD",True)if notselected:print("Failed to select GBPUSD")mt5.shutdown()quit()# display the last GBPUSD ticklasttick=mt5.symbol_info_tick("GBPUSD")print(lasttick)# display tick field values in the form of a listprint("Show symbol_info_tick(\"GBPUSD\")._asdict():")symbol_info_tick_dict =mt5.symbol_info_tick("GBPUSD")._asdict()forpropinsymbol_info_tick_dict:print("  {}={}".format(prop, symbol_info_tick_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)Show symbol_info_tick._asdict():time=1585070338bid=1.17264ask=1.17279last=0.0volume=0time_msc=1585070338728flags=2volume_real=0.0
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the GBPUSD in MarketWatchselected=mt5.symbol_select("GBPUSD",True)if notselected:print("Failed to select GBPUSD")mt5.shutdown()quit()# display the last GBPUSD ticklasttick=mt5.symbol_info_tick("GBPUSD")print(lasttick)# display tick field values in the form of a listprint("Show symbol_info_tick(\"GBPUSD\")._asdict():")symbol_info_tick_dict =mt5.symbol_info_tick("GBPUSD")._asdict()forpropinsymbol_info_tick_dict:print("  {}={}".format(prop, symbol_info_tick_dict[prop]))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)Show symbol_info_tick._asdict():time=1585070338bid=1.17264ask=1.17279last=0.0volume=0time_msc=1585070338728flags=2volume_real=0.0
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# attempt to enable the display of the GBPUSD in MarketWatch
selected
=
mt5.symbol_select
(
"GBPUSD"
,
True
)
if not
selected
:
print
(
"Failed to select GBPUSD"
)
mt5
.
shutdown
()
quit()
# display the last GBPUSD tick
lasttick
=
mt5.symbol_info_tick
(
"GBPUSD"
)
print
(
lasttick
)
# display tick field values in the form of a list
print
(
"Show symbol_info_tick(\"GBPUSD\")._asdict():"
)
symbol_info_tick_dict =
mt5.symbol_info_tick
(
"GBPUSD"
)
._asdict
()
for
prop
in
symbol_info_tick_dict:
print
(
"  {}={}"
.
format
(prop, symbol_info_tick_dict[prop]))
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Tick(time=1585070338, bid=1.17264, ask=1.17279, last=0.0, volume=0, time_msc=1585070338728, flags=2, volume_real=0.0)
Show symbol_info_tick._asdict():
time=1585070338
bid=1.17264
ask=1.17279
last=0.0
volume=0
time_msc=1585070338728
flags=2
volume_real=0.0

---

## symbol_select

Select a symbol in theMarketWatchwindow or remove a symbol from the window.

**Return Value**

True if successful, otherwise – False.
True if successful, otherwise – False.

**Example**

importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURCAD in MarketWatchselected=mt5.symbol_select("EURCAD",True)if notselected:print("Failed to select EURCAD, error code =",mt5.last_error())else:symbol_info=mt5.symbol_info("EURCAD")print(symbol_info)print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)print()# get symbol properties in the form of a dictionaryprint("Show symbol_info()._asdict():")symbol_info_dict =symbol_info._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])print("symbol_info_dict() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EURShow symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585217595digits=5spread=39spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=1.55192bidhigh=1.55842bidlow=1.5419800000000001ask=1.5523099999999999askhigh=1.55915asklow=1.5436299999999998last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=1e-05trade_tick_value=0.7043642408362214trade_tick_value_profit=0.7043642408362214trade_tick_value_loss=0.7044535553770941trade_tick_size=1e-05trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-1.1swap_short=-0.9margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=CADcurrency_margin=EURbank=description=Euro vs Canadian Dollarexchange=formula=isin=name=EURCADpage=http://www.google.com/finance?q=EURCADpath=Forex\EURCADsymbol_info_dict() as dataframe:property                                   value0          custom                                   False1      chart_mode                                       02          select                                    True3         visible                                    True4   session_deals                                       0..            ...                                     ...91        formula92           isin93           name                                  EURCAD94           page  http://www.google.com/finance?q=EURCAD95           path                            Forex\EURCAD[96 rows x 2 columns]
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURCAD in MarketWatchselected=mt5.symbol_select("EURCAD",True)if notselected:print("Failed to select EURCAD, error code =",mt5.last_error())else:symbol_info=mt5.symbol_info("EURCAD")print(symbol_info)print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)print()# get symbol properties in the form of a dictionaryprint("Show symbol_info()._asdict():")symbol_info_dict =symbol_info._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])print("symbol_info_dict() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EURShow symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585217595digits=5spread=39spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=1.55192bidhigh=1.55842bidlow=1.5419800000000001ask=1.5523099999999999askhigh=1.55915asklow=1.5436299999999998last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=1e-05trade_tick_value=0.7043642408362214trade_tick_value_profit=0.7043642408362214trade_tick_value_loss=0.7044535553770941trade_tick_size=1e-05trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-1.1swap_short=-0.9margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=CADcurrency_margin=EURbank=description=Euro vs Canadian Dollarexchange=formula=isin=name=EURCADpage=http://www.google.com/finance?q=EURCADpath=Forex\EURCADsymbol_info_dict() as dataframe:property                                   value0          custom                                   False1      chart_mode                                       02          select                                    True3         visible                                    True4   session_deals                                       0..            ...                                     ...91        formula92           isin93           name                                  EURCAD94           page  http://www.google.com/finance?q=EURCAD95           path                            Forex\EURCAD[96 rows x 2 columns]
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURCAD in MarketWatchselected=mt5.symbol_select("EURCAD",True)if notselected:print("Failed to select EURCAD, error code =",mt5.last_error())else:symbol_info=mt5.symbol_info("EURCAD")print(symbol_info)print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)print()# get symbol properties in the form of a dictionaryprint("Show symbol_info()._asdict():")symbol_info_dict =symbol_info._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])print("symbol_info_dict() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EURShow symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585217595digits=5spread=39spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=1.55192bidhigh=1.55842bidlow=1.5419800000000001ask=1.5523099999999999askhigh=1.55915asklow=1.5436299999999998last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=1e-05trade_tick_value=0.7043642408362214trade_tick_value_profit=0.7043642408362214trade_tick_value_loss=0.7044535553770941trade_tick_size=1e-05trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-1.1swap_short=-0.9margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=CADcurrency_margin=EURbank=description=Euro vs Canadian Dollarexchange=formula=isin=name=EURCADpage=http://www.google.com/finance?q=EURCADpath=Forex\EURCADsymbol_info_dict() as dataframe:property                                   value0          custom                                   False1      chart_mode                                       02          select                                    True3         visible                                    True4   session_deals                                       0..            ...                                     ...91        formula92           isin93           name                                  EURCAD94           page  http://www.google.com/finance?q=EURCAD95           path                            Forex\EURCAD[96 rows x 2 columns]
importMetaTrader5asmt5importpandasaspd# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):print("initialize() failed, error code =",mt5.last_error())quit()# attempt to enable the display of the EURCAD in MarketWatchselected=mt5.symbol_select("EURCAD",True)if notselected:print("Failed to select EURCAD, error code =",mt5.last_error())else:symbol_info=mt5.symbol_info("EURCAD")print(symbol_info)print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)print()# get symbol properties in the form of a dictionaryprint("Show symbol_info()._asdict():")symbol_info_dict =symbol_info._asdict()forpropinsymbol_info_dict:print("  {}={}".format(prop, symbol_info_dict[prop]))print()# convert the dictionary into DataFrame and printdf=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])print("symbol_info_dict() as dataframe:")print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EURShow symbol_info()._asdict():custom=Falsechart_mode=0select=Truevisible=Truesession_deals=0session_buy_orders=0session_sell_orders=0volume=0volumehigh=0volumelow=0time=1585217595digits=5spread=39spread_float=Trueticks_bookdepth=10trade_calc_mode=0trade_mode=4start_time=0expiration_time=0trade_stops_level=0trade_freeze_level=0trade_exemode=1swap_mode=1swap_rollover3days=3margin_hedged_use_leg=Falseexpiration_mode=7filling_mode=1order_mode=127order_gtc_mode=0option_mode=0option_right=0bid=1.55192bidhigh=1.55842bidlow=1.5419800000000001ask=1.5523099999999999askhigh=1.55915asklow=1.5436299999999998last=0.0lasthigh=0.0lastlow=0.0volume_real=0.0volumehigh_real=0.0volumelow_real=0.0option_strike=0.0point=1e-05trade_tick_value=0.7043642408362214trade_tick_value_profit=0.7043642408362214trade_tick_value_loss=0.7044535553770941trade_tick_size=1e-05trade_contract_size=100000.0trade_accrued_interest=0.0trade_face_value=0.0trade_liquidity_rate=0.0volume_min=0.01volume_max=500.0volume_step=0.01volume_limit=0.0swap_long=-1.1swap_short=-0.9margin_initial=0.0margin_maintenance=0.0session_volume=0.0session_turnover=0.0session_interest=0.0session_buy_orders_volume=0.0session_sell_orders_volume=0.0session_open=0.0session_close=0.0session_aw=0.0session_price_settlement=0.0session_price_limit_min=0.0session_price_limit_max=0.0margin_hedged=100000.0price_change=0.0price_volatility=0.0price_theoretical=0.0price_greeks_delta=0.0price_greeks_theta=0.0price_greeks_gamma=0.0price_greeks_vega=0.0price_greeks_rho=0.0price_greeks_omega=0.0price_sensitivity=0.0basis=category=currency_base=EURcurrency_profit=CADcurrency_margin=EURbank=description=Euro vs Canadian Dollarexchange=formula=isin=name=EURCADpage=http://www.google.com/finance?q=EURCADpath=Forex\EURCADsymbol_info_dict() as dataframe:property                                   value0          custom                                   False1      chart_mode                                       02          select                                    True3         visible                                    True4   session_deals                                       0..            ...                                     ...91        formula92           isin93           name                                  EURCAD94           page  http://www.google.com/finance?q=EURCAD95           path                            Forex\EURCAD[96 rows x 2 columns]
import
MetaTrader5
as
mt5
import
pandas
as
pd
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
()
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
(login=25115284, server=
"MetaQuotes-Demo"
,password=
"4zatlbqx"
):
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# attempt to enable the display of the EURCAD in MarketWatch
selected
=
mt5.symbol_select
(
"EURCAD"
,
True
)
if not
selected
:
print
(
"Failed to select EURCAD, error code ="
,
mt5.last_error()
)
else
:
symbol_info
=
mt5.symbol_info
(
"EURCAD"
)
print
(
symbol_info
)
print
(
"EURCAD: currency_base =",
symbol_info.currency_base,
"  currency_profit ="
,symbol_info.currency_profit,
"  currency_margin ="
,symbol_info.currency_margin
)
print
()
# get symbol properties in the form of a dictionary
print
(
"Show symbol_info()._asdict():"
)
symbol_info_dict =
symbol_info._asdict()
for
prop
in
symbol_info_dict:
print
(
"  {}={}"
.
format
(prop, symbol_info_dict[prop]))
print
()
# convert the dictionary into DataFrame and print
df
=pd.DataFrame
(
list
(symbol_info_dict.items()),columns=['property','value'])
print
(
"symbol_info_dict() as dataframe:"
)
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
SymbolInfo(custom=False, chart_mode=0, select=True, visible=True, session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0, volumehigh=0, ....
EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EUR
Show symbol_info()._asdict():
custom=False
chart_mode=0
select=True
visible=True
session_deals=0
session_buy_orders=0
session_sell_orders=0
volume=0
volumehigh=0
volumelow=0
time=1585217595
digits=5
spread=39
spread_float=True
ticks_bookdepth=10
trade_calc_mode=0
trade_mode=4
start_time=0
expiration_time=0
trade_stops_level=0
trade_freeze_level=0
trade_exemode=1
swap_mode=1
swap_rollover3days=3
margin_hedged_use_leg=False
expiration_mode=7
filling_mode=1
order_mode=127
order_gtc_mode=0
option_mode=0
option_right=0
bid=1.55192
bidhigh=1.55842
bidlow=1.5419800000000001
ask=1.5523099999999999
askhigh=1.55915
asklow=1.5436299999999998
last=0.0
lasthigh=0.0
lastlow=0.0
volume_real=0.0
volumehigh_real=0.0
volumelow_real=0.0
option_strike=0.0
point=1e-05
trade_tick_value=0.7043642408362214
trade_tick_value_profit=0.7043642408362214
trade_tick_value_loss=0.7044535553770941
trade_tick_size=1e-05
trade_contract_size=100000.0
trade_accrued_interest=0.0
trade_face_value=0.0
trade_liquidity_rate=0.0
volume_min=0.01
volume_max=500.0
volume_step=0.01
volume_limit=0.0
swap_long=-1.1
swap_short=-0.9
margin_initial=0.0
margin_maintenance=0.0
session_volume=0.0
session_turnover=0.0
session_interest=0.0
session_buy_orders_volume=0.0
session_sell_orders_volume=0.0
session_open=0.0
session_close=0.0
session_aw=0.0
session_price_settlement=0.0
session_price_limit_min=0.0
session_price_limit_max=0.0
margin_hedged=100000.0
price_change=0.0
price_volatility=0.0
price_theoretical=0.0
price_greeks_delta=0.0
price_greeks_theta=0.0
price_greeks_gamma=0.0
price_greeks_vega=0.0
price_greeks_rho=0.0
price_greeks_omega=0.0
price_sensitivity=0.0
basis=
category=
currency_base=EUR
currency_profit=CAD
currency_margin=EUR
bank=
description=Euro vs Canadian Dollar
exchange=
formula=
isin=
name=EURCAD
page=http://www.google.com/finance?q=EURCAD
path=Forex\EURCAD
symbol_info_dict() as dataframe:
property                                   value
0          custom                                   False
1      chart_mode                                       0
2          select                                    True
3         visible                                    True
4   session_deals                                       0
..            ...                                     ...
91        formula
92           isin
93           name                                  EURCAD
94           page  http://www.google.com/finance?q=EURCAD
95           path                            Forex\EURCAD
[96 rows x 2 columns]

---

## market_book_add

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

**Return Value**

True if successful, otherwise – False.
True if successful, otherwise – False.

---

## market_book_get

Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

**Return Value**

Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots. BookInfo is similar to theMqlBookInfostructure.
Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots. BookInfo is similar to theMqlBookInfostructure.
Return None in case of an error. The info on the error can be obtained usinglast_error().
Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importtime# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print("")# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()quit()# subscribe to market depth updates for EURUSD (Depth of Market)ifmt5.market_book_add('EURUSD'):# get the market depth data 10 times in a loopforiinrange(10):# get the market depth content (Depth of Market)items =mt5.market_book_get('EURUSD')# display the entire market depth 'as is' in a single stringprint(items)# now display each order separately for more clarityifitems:foritinitems:# order contentprint(it._asdict())# pause for 5 seconds before the next request of the market depth datatime.sleep(5)# cancel the subscription to the market depth updates (Depth of Market)mt5.market_book_release('EURUSD')else:print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.34(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}
importMetaTrader5asmt5importtime# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print("")# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()quit()# subscribe to market depth updates for EURUSD (Depth of Market)ifmt5.market_book_add('EURUSD'):# get the market depth data 10 times in a loopforiinrange(10):# get the market depth content (Depth of Market)items =mt5.market_book_get('EURUSD')# display the entire market depth 'as is' in a single stringprint(items)# now display each order separately for more clarityifitems:foritinitems:# order contentprint(it._asdict())# pause for 5 seconds before the next request of the market depth datatime.sleep(5)# cancel the subscription to the market depth updates (Depth of Market)mt5.market_book_release('EURUSD')else:print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.34(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}
importMetaTrader5asmt5importtime# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print("")# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()quit()# subscribe to market depth updates for EURUSD (Depth of Market)ifmt5.market_book_add('EURUSD'):# get the market depth data 10 times in a loopforiinrange(10):# get the market depth content (Depth of Market)items =mt5.market_book_get('EURUSD')# display the entire market depth 'as is' in a single stringprint(items)# now display each order separately for more clarityifitems:foritinitems:# order contentprint(it._asdict())# pause for 5 seconds before the next request of the market depth datatime.sleep(5)# cancel the subscription to the market depth updates (Depth of Market)mt5.market_book_release('EURUSD')else:print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.34(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}
importMetaTrader5asmt5importtime# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print("")# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()quit()# subscribe to market depth updates for EURUSD (Depth of Market)ifmt5.market_book_add('EURUSD'):# get the market depth data 10 times in a loopforiinrange(10):# get the market depth content (Depth of Market)items =mt5.market_book_get('EURUSD')# display the entire market depth 'as is' in a single stringprint(items)# now display each order separately for more clarityifitems:foritinitems:# order contentprint(it._asdict())# pause for 5 seconds before the next request of the market depth datatime.sleep(5)# cancel the subscription to the market depth updates (Depth of Market)mt5.market_book_release('EURUSD')else:print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.34(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}
import
MetaTrader5
as
mt5
import
time
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
(
""
)
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
quit()
# subscribe to market depth updates for EURUSD (Depth of Market)
if
mt5.market_book_add
(
'EURUSD'
):
# get the market depth data 10 times in a loop
for
i
in
range(10):
# get the market depth content (Depth of Market)
items =
mt5.market_book_get
(
'EURUSD'
)
# display the entire market depth 'as is' in a single string
print
(items)
# now display each order separately for more clarity
if
items:
for
it
in
items:
# order content
print(it.
_asdict
())
# pause for 5 seconds before the next request of the market depth data
time
.
sleep
(5)
# cancel the subscription to the market depth updates (Depth of Market)
mt5.market_book_release
(
'EURUSD'
)
else:
print
(
"mt5.market_book_add('EURUSD') failed, error code ="
,
mt5.last_error()
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.34
(BookInfo(type=1, price=1.20038, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20032, volume=100, volume...
{'type': 1, 'price': 1.20038, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20032, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20025, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20023, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20017, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...
{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.2004299999999999, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20037, volume...
{'type': 1, 'price': 1.2004299999999999, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20037, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20036, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20034, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20031, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20029, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20028, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20022, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20036, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...
{'type': 1, 'price': 1.20036, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20028, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20026, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20035, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20029, volume=100, volume...
{'type': 1, 'price': 1.20035, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20029, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.20027, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20022, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20021, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20014, 'volume': 250, 'volume_dbl': 250.0}
(BookInfo(type=1, price=1.20037, volume=250, volume_dbl=250.0), BookInfo(type=1, price=1.20031, volume=100, volume...
{'type': 1, 'price': 1.20037, 'volume': 250, 'volume_dbl': 250.0}
{'type': 1, 'price': 1.20031, 'volume': 100, 'volume_dbl': 100.0}
{'type': 1, 'price': 1.2003, 'volume': 50, 'volume_dbl': 50.0}
{'type': 1, 'price': 1.20028, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20025, 'volume': 36, 'volume_dbl': 36.0}
{'type': 2, 'price': 1.20023, 'volume': 50, 'volume_dbl': 50.0}
{'type': 2, 'price': 1.20022, 'volume': 100, 'volume_dbl': 100.0}
{'type': 2, 'price': 1.20016, 'volume': 250, 'volume_dbl': 250.0}

---

## market_book_release

Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

**Return Value**

True if successful, otherwise – False.
True if successful, otherwise – False.

---

## copy_rates_from

Get bars from the MetaTrader 5 terminal starting from the specified date.

**Parameters**

symbol
symbol
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
timeframe
timeframe
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
date_from
date_from
[in]  Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
count
count
[in]  Number of bars to receive. Required unnamed parameter.
[in]  Number of bars to receive. Required unnamed parameter.

**Return Value**

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Return None in case of an error. The info on the error can be obtained usinglast_error().
Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zonerates=mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_H4,utc_from,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            01 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            02 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            03 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            04 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            05 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            06 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            07 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            08 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            09 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zonerates=mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_H4,utc_from,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            01 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            02 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            03 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            04 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            05 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            06 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            07 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            08 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            09 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zonerates=mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_H4,utc_from,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            01 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            02 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            03 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            04 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            05 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            06 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            07 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            08 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            09 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zonerates=mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_H4,utc_from,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            01 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            02 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            03 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            04 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            05 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            06 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            07 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            08 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            09 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# import the 'pandas' module for displaying data obtained in the tabular form
import
pandas
as
pd
pd
.
set_option
('
display
.
max_columns
',
500
)
# number of columns to be displayed
pd
.
set_option
('
display
.
width
',
1500
)
# max table width to display
# import pytz module for working with time zone
import
pytz
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# set time zone to UTC
timezone
=
pytz
.
timezone
(
"Etc/UTC"
)
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from
=
datetime
(
2020
, 1, 10,
tzinfo
=
timezone
)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates
=
mt5.copy_rates_from
(
"EURUSD"
,
mt5.TIMEFRAME_H4
,
utc_from
,
10
)
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()
# display each element of obtained data in a new line
print
(
"Display obtained data 'as is'"
)
for
rate
in
rates
:
print
(
rate
)
# create DataFrame out of the obtained data
rates_frame
=
pd
.
DataFrame
(
rates
)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'],
unit
='s')
# display data
print
(
"\nDisplay dataframe with data"
)
print
(
rates_frame
)
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Display obtained data 'as is'
(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)
(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)
(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)
(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)
(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)
(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)
(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)
(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)
(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)
(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)
Display dataframe with data
time     open     high      low    close  tick_volume  spread  real_volume
0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1            0
1 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1            0
2 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1            0
3 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1            0
4 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1            0
5 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1            0
6 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1            0
7 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1            0
8 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1            0
9 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1            0

---

## copy_rates_from_pos

Get bars from the MetaTrader 5 terminal starting from the specified index.

**Parameters**

symbol
symbol
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
timeframe
timeframe
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
start_pos
start_pos
[in]  Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter.
[in]  Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter.
count
count
[in]  Number of bars to receive. Required unnamed parameter.
[in]  Number of bars to receive. Required unnamed parameter.

**Return Value**

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained usinglast_error().
Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get 10 GBPUSD D1 bars from the current dayrates=mt5.copy_rates_from_pos("GBPUSD",mt5.TIMEFRAME_D1,0,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            01 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            02 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            03 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            04 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            05 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            06 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            07 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            08 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            09 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get 10 GBPUSD D1 bars from the current dayrates=mt5.copy_rates_from_pos("GBPUSD",mt5.TIMEFRAME_D1,0,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            01 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            02 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            03 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            04 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            05 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            06 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            07 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            08 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            09 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get 10 GBPUSD D1 bars from the current dayrates=mt5.copy_rates_from_pos("GBPUSD",mt5.TIMEFRAME_D1,0,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            01 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            02 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            03 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            04 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            05 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            06 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            07 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            08 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            09 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get 10 GBPUSD D1 bars from the current dayrates=mt5.copy_rates_from_pos("GBPUSD",mt5.TIMEFRAME_D1,0,10)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")forrateinrates:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the datetime formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame)Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            01 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            02 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            03 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            04 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            05 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            06 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            07 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            08 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            09 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# import the 'pandas' module for displaying data obtained in the tabular form
import
pandas
as
pd
pd
.
set_option
('
display
.
max_columns
',
500
)
# number of columns to be displayed
pd
.
set_option
('
display
.
width
',
1500
)
# max table width to display
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get 10 GBPUSD D1 bars from the current day
rates
=
mt5.copy_rates_from_pos
(
"GBPUSD"
,
mt5.TIMEFRAME_D1
,
0
,
10
)
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()
# display each element of obtained data in a new line
print
(
"Display obtained data 'as is'"
)
for
rate
in
rates
:
print
(
rate
)
# create DataFrame out of the obtained data
rates_frame
=
pd
.
DataFrame
(
rates
)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'],
unit
='s')
# display data
print
(
"\nDisplay dataframe with data"
)
print
(
rates_frame
)
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Display obtained data 'as is'
(1581552000, 1.29568, 1.30692, 1.29441, 1.30412, 68228, 0, 0)
(1581638400, 1.30385, 1.30631, 1.3001, 1.30471, 56498, 0, 0)
(1581897600, 1.30324, 1.30536, 1.29975, 1.30039, 49400, 0, 0)
(1581984000, 1.30039, 1.30486, 1.29705, 1.29952, 62288, 0, 0)
(1582070400, 1.29952, 1.3023, 1.29075, 1.29187, 57909, 0, 0)
(1582156800, 1.29186, 1.29281, 1.28489, 1.28792, 61033, 0, 0)
(1582243200, 1.28802, 1.29805, 1.28746, 1.29566, 66386, 0, 0)
(1582502400, 1.29426, 1.29547, 1.28865, 1.29283, 66933, 0, 0)
(1582588800, 1.2929, 1.30178, 1.29142, 1.30037, 80121, 0, 0)
(1582675200, 1.30036, 1.30078, 1.29136, 1.29374, 49286, 0, 0)
Display dataframe with data
time     open     high      low    close  tick_volume  spread  real_volume
0 2020-02-13  1.29568  1.30692  1.29441  1.30412        68228       0            0
1 2020-02-14  1.30385  1.30631  1.30010  1.30471        56498       0            0
2 2020-02-17  1.30324  1.30536  1.29975  1.30039        49400       0            0
3 2020-02-18  1.30039  1.30486  1.29705  1.29952        62288       0            0
4 2020-02-19  1.29952  1.30230  1.29075  1.29187        57909       0            0
5 2020-02-20  1.29186  1.29281  1.28489  1.28792        61033       0            0
6 2020-02-21  1.28802  1.29805  1.28746  1.29566        66386       0            0
7 2020-02-24  1.29426  1.29547  1.28865  1.29283        66933       0            0
8 2020-02-25  1.29290  1.30178  1.29142  1.30037        80121       0            0
9 2020-02-26  1.30036  1.30078  1.29136  1.29374        49286       0            0

---

## copy_rates_range

Get bars in the specified date range from the MetaTrader 5 terminal.

**Parameters**

symbol
symbol
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
timeframe
timeframe
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
[in]  Timeframe the bars are requested for. Set by a value from theTIMEFRAMEenumeration. Required unnamed parameter.
date_from
date_from
[in]  Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter.
[in]  Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time >= date_from are returned. Required unnamed parameter.
date_to
date_to
[in]  Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter.
[in]  Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Bars with the open time <= date_to are returned. Required unnamed parameter.

**Return Value**

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained usinglast_error().
Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, hour = 13, tzinfo=timezone)# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zonerates=mt5.copy_rates_range("USDJPY",mt5.TIMEFRAME_M5,utc_from, utc_to)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")counter=0forrateinrates:counter+=1ifcounter<=10:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the 'datetime' formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            01 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            02 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            03 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            04 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            05 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            06 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            07 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            08 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            09 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, hour = 13, tzinfo=timezone)# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zonerates=mt5.copy_rates_range("USDJPY",mt5.TIMEFRAME_M5,utc_from, utc_to)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")counter=0forrateinrates:counter+=1ifcounter<=10:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the 'datetime' formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            01 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            02 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            03 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            04 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            05 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            06 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            07 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            08 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            09 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, hour = 13, tzinfo=timezone)# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zonerates=mt5.copy_rates_range("USDJPY",mt5.TIMEFRAME_M5,utc_from, utc_to)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")counter=0forrateinrates:counter+=1ifcounter<=10:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the 'datetime' formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            01 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            02 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            03 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            04 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            05 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            06 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            07 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            08 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            09 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, hour = 13, tzinfo=timezone)# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zonerates=mt5.copy_rates_range("USDJPY",mt5.TIMEFRAME_M5,utc_from, utc_to)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display each element of obtained data in a new lineprint("Display obtained data 'as is'")counter=0forrateinrates:counter+=1ifcounter<=10:print(rate)# create DataFrame out of the obtained datarates_frame=pd.DataFrame(rates)# convert time in seconds into the 'datetime' formatrates_frame['time']=pd.to_datetime(rates_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with data")print(rates_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Display obtained data 'as is'(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)Display dataframe with datatime     open     high      low    close  tick_volume  spread  real_volume0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            01 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            02 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            03 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            04 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            05 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            06 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            07 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            08 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            09 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# import the 'pandas' module for displaying data obtained in the tabular form
import
pandas
as
pd
pd
.
set_option
('
display
.
max_columns
',
500
)
# number of columns to be displayed
pd
.
set_option
('
display
.
width
',
1500
)
# max table width to display
# import pytz module for working with time zone
import
pytz
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# set time zone to UTC
timezone
=
pytz
.
timezone
(
"Etc/UTC"
)
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from
=
datetime
(
2020
, 1, 10,
tzinfo
=
timezone
)
utc_to =
datetime
(2020, 1, 11, hour = 13, tzinfo=timezone)
# get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates
=
mt5.copy_rates_range
(
"USDJPY"
,
mt5.TIMEFRAME_M5
,
utc_from
, utc_to)
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()
# display each element of obtained data in a new line
print
(
"Display obtained data 'as is'"
)
counter=0
for
rate
in
rates
:
counter+=1
if
counter<=10:
print
(
rate
)
# create DataFrame out of the obtained data
rates_frame
=
pd
.
DataFrame
(
rates
)
# convert time in seconds into the 'datetime' format
rates_frame['time']=pd.to_datetime(rates_frame['time'],
unit
='s')
# display data
print
(
"\nDisplay dataframe with data"
)
print
(
rates_frame.head(
10
)
)
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Display obtained data 'as is'
(1578614400, 109.513, 109.527, 109.505, 109.521, 43, 2, 0)
(1578614700, 109.521, 109.549, 109.518, 109.543, 215, 8, 0)
(1578615000, 109.543, 109.543, 109.466, 109.505, 98, 10, 0)
(1578615300, 109.504, 109.534, 109.502, 109.517, 155, 8, 0)
(1578615600, 109.517, 109.539, 109.513, 109.527, 71, 4, 0)
(1578615900, 109.526, 109.537, 109.484, 109.52, 106, 9, 0)
(1578616200, 109.52, 109.524, 109.508, 109.51, 205, 7, 0)
(1578616500, 109.51, 109.51, 109.491, 109.496, 44, 8, 0)
(1578616800, 109.496, 109.509, 109.487, 109.5, 85, 5, 0)
(1578617100, 109.5, 109.504, 109.487, 109.489, 82, 7, 0)
Display dataframe with data
time     open     high      low    close  tick_volume  spread  real_volume
0 2020-01-10 00:00:00  109.513  109.527  109.505  109.521           43       2            0
1 2020-01-10 00:05:00  109.521  109.549  109.518  109.543          215       8            0
2 2020-01-10 00:10:00  109.543  109.543  109.466  109.505           98      10            0
3 2020-01-10 00:15:00  109.504  109.534  109.502  109.517          155       8            0
4 2020-01-10 00:20:00  109.517  109.539  109.513  109.527           71       4            0
5 2020-01-10 00:25:00  109.526  109.537  109.484  109.520          106       9            0
6 2020-01-10 00:30:00  109.520  109.524  109.508  109.510          205       7            0
7 2020-01-10 00:35:00  109.510  109.510  109.491  109.496           44       8            0
8 2020-01-10 00:40:00  109.496  109.509  109.487  109.500           85       5            0
9 2020-01-10 00:45:00  109.500  109.504  109.487  109.489           82       7            0

---

## copy_ticks_from

Get ticks from the MetaTrader 5 terminal starting from the specified date.

**Parameters**

symbol
symbol
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
from
from
[in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
count
count
[in]  Number of ticks to receive. Required unnamed parameter.
[in]  Number of ticks to receive. Required unnamed parameter.
flags
flags
[in]  A flag to define the type of the requested ticks.COPY_TICKS_INFO– ticks with Bid and/or Ask changes,COPY_TICKS_TRADE– ticks with changes in Last and Volume,COPY_TICKS_ALL– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter.
[in]  A flag to define the type of the requested ticks.
COPY_TICKS_INFO
– ticks with Bid and/or Ask changes,
COPY_TICKS_TRADE
– ticks with changes in Last and Volume,
COPY_TICKS_ALL
– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter.

**Return Value**

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from theTICK_FLAGenumeration. Return None in case of an error. The info on the error can be obtained usinglast_error().
Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from theTICK_FLAGenumeration. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zoneticks =mt5.copy_ticks_from("EURUSD",utc_from,100000,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 100000Display obtained ticks 'as is'(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.01 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.02 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.03 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.04 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.05 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.06 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.07 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.08 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.09 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zoneticks =mt5.copy_ticks_from("EURUSD",utc_from,100000,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 100000Display obtained ticks 'as is'(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.01 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.02 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.03 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.04 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.05 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.06 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.07 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.08 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.09 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zoneticks =mt5.copy_ticks_from("EURUSD",utc_from,100000,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 100000Display obtained ticks 'as is'(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.01 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.02 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.03 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.04 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.05 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.06 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.07 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.08 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.09 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zoneticks =mt5.copy_ticks_from("EURUSD",utc_from,100000,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 100000Display obtained ticks 'as is'(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.01 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.02 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.03 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.04 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.05 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.06 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.07 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.08 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.09 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# import the 'pandas' module for displaying data obtained in the tabular form
import
pandas
as
pd
pd
.
set_option
('
display
.
max_columns
',
500
)
# number of columns to be displayed
pd
.
set_option
('
display
.
width
',
1500
)
# max table width to display
# import pytz module for working with time zone
import
pytz
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# set time zone to UTC
timezone
=
pytz
.
timezone
(
"Etc/UTC"
)
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from
=
datetime
(
2020
, 1, 10,
tzinfo
=
timezone
)
# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
ticks =
mt5.copy_ticks_from
(
"EURUSD"
,
utc_from
,
100000,
mt5.COPY_TICKS_ALL
)
print
("Ticks received:",len(ticks))
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()
# display data on each tick on a new line
print
(
"Display obtained ticks 'as is'"
)
count = 0
for
tick
in
ticks
:
count+=1
print
(
tick
)
if
count >= 10:
break
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(
ticks_frame
['time'],
unit
='s')
# display data
print
(
"\nDisplay dataframe with ticks"
)
print
(
ticks_frame.head(10)
)
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Ticks received: 100000
Display obtained ticks 'as is'
(1578614400, 1.11051, 1.11069, 0., 0, 1578614400987, 134, 0.)
(1578614402, 1.11049, 1.11067, 0., 0, 1578614402025, 134, 0.)
(1578614404, 1.1105, 1.11066, 0., 0, 1578614404057, 134, 0.)
(1578614404, 1.11049, 1.11067, 0., 0, 1578614404344, 134, 0.)
(1578614412, 1.11052, 1.11064, 0., 0, 1578614412106, 134, 0.)
(1578614418, 1.11039, 1.11051, 0., 0, 1578614418265, 134, 0.)
(1578614418, 1.1104, 1.1105, 0., 0, 1578614418905, 134, 0.)
(1578614419, 1.11039, 1.11051, 0., 0, 1578614419519, 134, 0.)
(1578614456, 1.11037, 1.11065, 0., 0, 1578614456011, 134, 0.)
(1578614456, 1.11039, 1.11051, 0., 0, 1578614456015, 134, 0.)
Display dataframe with ticks
time      bid      ask  last  volume       time_msc  flags  volume_real
0 2020-01-10 00:00:00  1.11051  1.11069   0.0       0  1578614400987    134          0.0
1 2020-01-10 00:00:02  1.11049  1.11067   0.0       0  1578614402025    134          0.0
2 2020-01-10 00:00:04  1.11050  1.11066   0.0       0  1578614404057    134          0.0
3 2020-01-10 00:00:04  1.11049  1.11067   0.0       0  1578614404344    134          0.0
4 2020-01-10 00:00:12  1.11052  1.11064   0.0       0  1578614412106    134          0.0
5 2020-01-10 00:00:18  1.11039  1.11051   0.0       0  1578614418265    134          0.0
6 2020-01-10 00:00:18  1.11040  1.11050   0.0       0  1578614418905    134          0.0
7 2020-01-10 00:00:19  1.11039  1.11051   0.0       0  1578614419519    134          0.0
8 2020-01-10 00:00:56  1.11037  1.11065   0.0       0  1578614456011    134          0.0
9 2020-01-10 00:00:56  1.11039  1.11051   0.0       0  1578614456015    134          0.0

---

## copy_ticks_range

Get ticks for the specified date range from the MetaTrader 5 terminal.

**Parameters**

symbol
symbol
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
[in]  Financial instrument name, for example, "EURUSD". Required unnamed parameter.
date_from
date_from
[in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date the ticks are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
date_to
date_to
[in]  Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date, up to which the ticks are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
flags
flags
[in]  A flag to define the type of the requested ticks.COPY_TICKS_INFO– ticks with Bid and/or Ask changes,COPY_TICKS_TRADE– ticks with changes in Last and Volume,COPY_TICKS_ALL– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter.
[in]  A flag to define the type of the requested ticks.
COPY_TICKS_INFO
– ticks with Bid and/or Ask changes,
COPY_TICKS_TRADE
– ticks with changes in Last and Volume,
COPY_TICKS_ALL
– all ticks. Flag values are described in theCOPY_TICKSenumeration. Required unnamed parameter.

**Return Value**

Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from theTICK_FLAGenumeration. Return None in case of an error. The info on the error can be obtained usinglast_error().
Returns ticks as the numpy array with the named time, bid, ask, last and flags columns. The 'flags' value can be a combination of flags from theTICK_FLAGenumeration. Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, tzinfo=timezone)# request AUDUSD ticks within 11.01.2020 - 11.01.2020ticks =mt5.copy_ticks_range("AUDUSD",utc_from, utc_to,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 37008Display obtained ticks 'as is'(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.01 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.02 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.03 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.04 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.05 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.06 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.07 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.08 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.09 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, tzinfo=timezone)# request AUDUSD ticks within 11.01.2020 - 11.01.2020ticks =mt5.copy_ticks_range("AUDUSD",utc_from, utc_to,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 37008Display obtained ticks 'as is'(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.01 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.02 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.03 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.04 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.05 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.06 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.07 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.08 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.09 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, tzinfo=timezone)# request AUDUSD ticks within 11.01.2020 - 11.01.2020ticks =mt5.copy_ticks_range("AUDUSD",utc_from, utc_to,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 37008Display obtained ticks 'as is'(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.01 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.02 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.03 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.04 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.05 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.06 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.07 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.08 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.09 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# import the 'pandas' module for displaying data obtained in the tabular formimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width',1500)# max table width to display# import pytz module for working with time zoneimportpytz# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# set time zone to UTCtimezone=pytz.timezone("Etc/UTC")# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offsetutc_from=datetime(2020, 1, 10,tzinfo=timezone)utc_to =datetime(2020, 1, 11, tzinfo=timezone)# request AUDUSD ticks within 11.01.2020 - 11.01.2020ticks =mt5.copy_ticks_range("AUDUSD",utc_from, utc_to,mt5.COPY_TICKS_ALL)print("Ticks received:",len(ticks))# shut down connection to the MetaTrader 5 terminalmt5.shutdown()# display data on each tick on a new lineprint("Display obtained ticks 'as is'")count = 0fortickinticks:count+=1print(tick)ifcount >= 10:break# create DataFrame out of the obtained dataticks_frame = pd.DataFrame(ticks)# convert time in seconds into the datetime formatticks_frame['time']=pd.to_datetime(ticks_frame['time'],unit='s')# display dataprint("\nDisplay dataframe with ticks")print(ticks_frame.head(10))Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Ticks received: 37008Display obtained ticks 'as is'(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)Display dataframe with tickstime      bid      ask  last  volume       time_msc  flags  volume_real0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.01 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.02 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.03 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.04 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.05 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.06 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.07 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.08 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.09 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# import the 'pandas' module for displaying data obtained in the tabular form
import
pandas
as
pd
pd
.
set_option
('
display
.
max_columns
',
500
)
# number of columns to be displayed
pd
.
set_option
('
display
.
width
',
1500
)
# max table width to display
# import pytz module for working with time zone
import
pytz
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# set time zone to UTC
timezone
=
pytz
.
timezone
(
"Etc/UTC"
)
# create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
utc_from
=
datetime
(
2020
, 1, 10,
tzinfo
=
timezone
)
utc_to =
datetime
(2020, 1, 11, tzinfo=timezone)
# request AUDUSD ticks within 11.01.2020 - 11.01.2020
ticks =
mt5.copy_ticks_range
(
"AUDUSD"
,
utc_from
, utc_to
,
mt5.COPY_TICKS_ALL
)
print
("Ticks received:",len(ticks))
# shut down connection to the MetaTrader 5 terminal
mt5
.
shutdown
()
# display data on each tick on a new line
print
(
"Display obtained ticks 'as is'"
)
count = 0
for
tick
in
ticks
:
count+=1
print
(
tick
)
if
count >= 10:
break
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(
ticks_frame
['time'],
unit
='s')
# display data
print
(
"\nDisplay dataframe with ticks"
)
print
(
ticks_frame.head(10)
)
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Ticks received: 37008
Display obtained ticks 'as is'
(1578614400, 0.68577, 0.68594, 0., 0, 1578614400820, 134, 0.)
(1578614401, 0.68578, 0.68594, 0., 0, 1578614401128, 130, 0.)
(1578614401, 0.68575, 0.68594, 0., 0, 1578614401128, 130, 0.)
(1578614411, 0.68576, 0.68594, 0., 0, 1578614411388, 130, 0.)
(1578614411, 0.68575, 0.68594, 0., 0, 1578614411560, 130, 0.)
(1578614414, 0.68576, 0.68595, 0., 0, 1578614414973, 134, 0.)
(1578614430, 0.68576, 0.68594, 0., 0, 1578614430188, 4, 0.)
(1578614450, 0.68576, 0.68595, 0., 0, 1578614450408, 4, 0.)
(1578614450, 0.68576, 0.68594, 0., 0, 1578614450519, 4, 0.)
(1578614456, 0.68575, 0.68594, 0., 0, 1578614456363, 130, 0.)
Display dataframe with ticks
time      bid      ask  last  volume       time_msc  flags  volume_real
0 2020-01-10 00:00:00  0.68577  0.68594   0.0       0  1578614400820    134          0.0
1 2020-01-10 00:00:01  0.68578  0.68594   0.0       0  1578614401128    130          0.0
2 2020-01-10 00:00:01  0.68575  0.68594   0.0       0  1578614401128    130          0.0
3 2020-01-10 00:00:11  0.68576  0.68594   0.0       0  1578614411388    130          0.0
4 2020-01-10 00:00:11  0.68575  0.68594   0.0       0  1578614411560    130          0.0
5 2020-01-10 00:00:14  0.68576  0.68595   0.0       0  1578614414973    134          0.0
6 2020-01-10 00:00:30  0.68576  0.68594   0.0       0  1578614430188      4          0.0
7 2020-01-10 00:00:50  0.68576  0.68595   0.0       0  1578614450408      4          0.0
8 2020-01-10 00:00:50  0.68576  0.68594   0.0       0  1578614450519      4          0.0
9 2020-01-10 00:00:56  0.68575  0.68594   0.0       0  1578614456363    130          0.0

---

## orders_total

Get the number of active orders.

**Return Value**

Integer value.
Integer value.

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of active ordersorders=mt5.orders_total()iforders>0:print("Total orders=",orders)else:print("Orders not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of active ordersorders=mt5.orders_total()iforders>0:print("Total orders=",orders)else:print("Orders not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of active ordersorders=mt5.orders_total()iforders>0:print("Total orders=",orders)else:print("Orders not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of active ordersorders=mt5.orders_total()iforders>0:print("Total orders=",orders)else:print("Orders not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# check the presence of active orders
orders
=
mt5.orders_total
()
if
orders>0
:
print
(
"Total orders=",
orders
)
else
:
print
(
"Orders not found"
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## orders_get

Get active orders with the ability to filter by symbol or ticket. There are three call options.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on active orders on GBPUSDorders=mt5.orders_get(symbol="GBPUSD")ifordersisNone:print("No orders on GBPUSD, error code={}".format(mt5.last_error()))else:print("Total orders on GBPUSD:",len(orders))# display all active ordersfororderinorders:print(order)print()# get the list of orders on symbols whose names contain "*GBP*"gbp_orders=mt5.orders_get(group="*GBP*")ifgbp_ordersisNone:print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))else:print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Total orders on GBPUSD: 2TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...orders_get(group="*GBP*")=4ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on active orders on GBPUSDorders=mt5.orders_get(symbol="GBPUSD")ifordersisNone:print("No orders on GBPUSD, error code={}".format(mt5.last_error()))else:print("Total orders on GBPUSD:",len(orders))# display all active ordersfororderinorders:print(order)print()# get the list of orders on symbols whose names contain "*GBP*"gbp_orders=mt5.orders_get(group="*GBP*")ifgbp_ordersisNone:print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))else:print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Total orders on GBPUSD: 2TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...orders_get(group="*GBP*")=4ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on active orders on GBPUSDorders=mt5.orders_get(symbol="GBPUSD")ifordersisNone:print("No orders on GBPUSD, error code={}".format(mt5.last_error()))else:print("Total orders on GBPUSD:",len(orders))# display all active ordersfororderinorders:print(order)print()# get the list of orders on symbols whose names contain "*GBP*"gbp_orders=mt5.orders_get(group="*GBP*")ifgbp_ordersisNone:print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))else:print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Total orders on GBPUSD: 2TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...orders_get(group="*GBP*")=4ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# display data on active orders on GBPUSDorders=mt5.orders_get(symbol="GBPUSD")ifordersisNone:print("No orders on GBPUSD, error code={}".format(mt5.last_error()))else:print("Total orders on GBPUSD:",len(orders))# display all active ordersfororderinorders:print(order)print()# get the list of orders on symbols whose names contain "*GBP*"gbp_orders=mt5.orders_get(group="*GBP*")ifgbp_ordersisNone:print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))else:print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Total orders on GBPUSD: 2TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...orders_get(group="*GBP*")=4ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP
import
MetaTrader5
as
mt5
import
pandas
as
pd
pd
.
set_option
(
'display.max_columns'
,
500
)
# number of columns to be displayed
pd
.
set_option
(
'display.width', 1500
)
# max table width to display
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
()
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# display data on active orders on GBPUSD
orders
=
mt5.orders_get
(symbol=
"GBPUSD"
)
if
orders
is
None
:
print
(
"No orders on GBPUSD, error code={}"
.format(
mt5.last_error()
))
else
:
print
(
"Total orders on GBPUSD:",
len(
orders)
)
# display all active orders
for
order
in
orders
:
print
(
order
)
print
()
# get the list of orders on symbols whose names contain "*GBP*"
gbp_orders
=
mt5.orders_get
(
group=
"*GBP*"
)
if
gbp_orders
is
None
:
print
(
"No orders with group=\"*GBP*\", error code={}"
.
format
(
mt5.last_error()
))
else
:
print
(
"orders_get(group=\"*GBP*\")={}"
.
format
(
len
(gbp_orders)
))
# display these orders as a table using pandas.DataFrame
df=
pd.DataFrame
(
list
(
gbp_orders
),columns=
gbp_orders
[0]._asdict().keys())
df.drop([
'time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'
], axis=1, inplace=
True
)
df[
'time_setup'
] = pd.to_datetime(df[
'time_setup'
], unit='s')
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Total orders on GBPUSD: 2
TradeOrder(ticket=554733548, time_setup=1585153667, time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0, type=3, type_time=0, ...
TradeOrder(ticket=554733621, time_setup=1585153671, time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0, type=2, type_time=0, ...
orders_get(group="*GBP*")=4
ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id
0  554733548 2020-03-25 16:27:47   1585153667718                0     3          0             2      1      0             0.2     1.25379  0.0  0.0        1.16803  GBPUSD
1  554733621 2020-03-25 16:27:51   1585153671419                0     2          0             2      1      0             0.2     1.14370  0.0  0.0        1.16815  GBPUSD
2  554746664 2020-03-25 16:38:14   1585154294401                0     3          0             2      1      0             0.2     0.93851  0.0  0.0        0.92428  EURGBP
3  554746710 2020-03-25 16:38:17   1585154297022                0     2          0             2      1      0             0.2     0.90527  0.0  0.0        0.92449  EURGBP

---

## order_calc_margin

Return margin in the account currency to perform a specified trading operation.

**Parameters**

action
action
[in]  Order type taking values from theORDER_TYPEenumeration. Required unnamed parameter.
[in]  Order type taking values from theORDER_TYPEenumeration. Required unnamed parameter.
symbol
symbol
[in]  Financial instrument name. Required unnamed parameter.
[in]  Financial instrument name. Required unnamed parameter.
volume
volume
[in]  Trading operation volume. Required unnamed parameter.
[in]  Trading operation volume. Required unnamed parameter.
price
price
[in]  Open price. Required unnamed parameter.
[in]  Open price. Required unnamed parameter.

**Return Value**

Real value if successful, otherwise None. The error info can be obtained usinglast_error().
Real value if successful, otherwise None. The error info can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols=("EURUSD","GBPUSD","USDJPY","USDCHF","EURJPY","GBPJPY")print("Symbols to check margin:", symbols)action=mt5.ORDER_TYPE_BUYlot=0.1forsymbolin symbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continueask=mt5.symbol_info_tick(symbol).askmargin=mt5.order_calc_margin(action,symbol,lot,ask)ifmargin !=None:print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));else:print("order_calc_margin failed: , error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')EURUSD buy 0.1 lot margin: 109.91 USDGBPUSD buy 0.1 lot margin: 122.73 USDUSDJPY buy 0.1 lot margin: 100.0 USDUSDCHF buy 0.1 lot margin: 100.0 USDEURJPY buy 0.1 lot margin: 109.91 USDGBPJPY buy 0.1 lot margin: 122.73 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols=("EURUSD","GBPUSD","USDJPY","USDCHF","EURJPY","GBPJPY")print("Symbols to check margin:", symbols)action=mt5.ORDER_TYPE_BUYlot=0.1forsymbolin symbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continueask=mt5.symbol_info_tick(symbol).askmargin=mt5.order_calc_margin(action,symbol,lot,ask)ifmargin !=None:print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));else:print("order_calc_margin failed: , error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')EURUSD buy 0.1 lot margin: 109.91 USDGBPUSD buy 0.1 lot margin: 122.73 USDUSDJPY buy 0.1 lot margin: 100.0 USDUSDCHF buy 0.1 lot margin: 100.0 USDEURJPY buy 0.1 lot margin: 109.91 USDGBPJPY buy 0.1 lot margin: 122.73 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols=("EURUSD","GBPUSD","USDJPY","USDCHF","EURJPY","GBPJPY")print("Symbols to check margin:", symbols)action=mt5.ORDER_TYPE_BUYlot=0.1forsymbolin symbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continueask=mt5.symbol_info_tick(symbol).askmargin=mt5.order_calc_margin(action,symbol,lot,ask)ifmargin !=None:print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));else:print("order_calc_margin failed: , error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')EURUSD buy 0.1 lot margin: 109.91 USDGBPUSD buy 0.1 lot margin: 122.73 USDUSDJPY buy 0.1 lot margin: 100.0 USDUSDCHF buy 0.1 lot margin: 100.0 USDEURJPY buy 0.1 lot margin: 109.91 USDGBPJPY buy 0.1 lot margin: 122.73 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols=("EURUSD","GBPUSD","USDJPY","USDCHF","EURJPY","GBPJPY")print("Symbols to check margin:", symbols)action=mt5.ORDER_TYPE_BUYlot=0.1forsymbolin symbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continueask=mt5.symbol_info_tick(symbol).askmargin=mt5.order_calc_margin(action,symbol,lot,ask)ifmargin !=None:print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));else:print("order_calc_margin failed: , error code =",mt5.last_error())# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')EURUSD buy 0.1 lot margin: 109.91 USDGBPUSD buy 0.1 lot margin: 122.73 USDUSDJPY buy 0.1 lot margin: 100.0 USDUSDCHF buy 0.1 lot margin: 100.0 USDEURJPY buy 0.1 lot margin: 109.91 USDGBPJPY buy 0.1 lot margin: 122.73 USD
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get account currency
account_currency=
mt5.account_info()
.currency
print
(
"Account currency:"
,account_currency)
# arrange the symbol list
symbols=(
"EURUSD"
,
"GBPUSD"
,
"USDJPY"
,
"USDCHF"
,
"EURJPY"
,
"GBPJPY"
)
print
("Symbols to check margin:", symbols)
action=
mt5.ORDER_TYPE_BUY
lot=0.1
for
symbol
in symbols:
symbol_info=
mt5.symbol_info
(symbol)
if
symbol_info is
None
:
print
(symbol,
"not found, skipped"
)
continue
if
not
symbol_info.visible:
print
(symbol,
"is not visible, trying to switch on"
)
if
not
mt5.symbol_select
(symbol,
True
):
print
(
"symbol_select({}}) failed, skipped"
,symbol)
continue
ask=
mt5.symbol_info_tick
(symbol).ask
margin=
mt5.order_calc_margin
(action,symbol,lot,ask)
if
margin !=
None
:
print
(
"   {} buy {} lot margin: {} {}"
.format(symbol,lot,margin,account_currency));
else
:
print
(
"order_calc_margin failed: , error code ="
,
mt5.last_error
())
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Account currency: USD
Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'EURJPY', 'GBPJPY')
EURUSD buy 0.1 lot margin: 109.91 USD
GBPUSD buy 0.1 lot margin: 122.73 USD
USDJPY buy 0.1 lot margin: 100.0 USD
USDCHF buy 0.1 lot margin: 100.0 USD
EURJPY buy 0.1 lot margin: 109.91 USD
GBPJPY buy 0.1 lot margin: 122.73 USD

---

## order_calc_profit

Return profit in the account currency for a specified trading operation.

**Parameters**

action
action
[in]  Order type may take one of the twoORDER_TYPEenumeration values: ORDER_TYPE_BUY or ORDER_TYPE_SELL. Required unnamed parameter.
[in]  Order type may take one of the twoORDER_TYPEenumeration values: ORDER_TYPE_BUY or ORDER_TYPE_SELL. Required unnamed parameter.
symbol
symbol
[in]  Financial instrument name. Required unnamed parameter.
[in]  Financial instrument name. Required unnamed parameter.
volume
volume
[in]  Trading operation volume. Required unnamed parameter.
[in]  Trading operation volume. Required unnamed parameter.
price_open
price_open
[in]  Open price. Required unnamed parameter.
[in]  Open price. Required unnamed parameter.
price_close
price_close
[in]  Close price. Required unnamed parameter.
[in]  Close price. Required unnamed parameter.

**Return Value**

Real value if successful, otherwise None. The error info can be obtained usinglast_error().
Real value if successful, otherwise None. The error info can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols = ("EURUSD","GBPUSD","USDJPY")print("Symbols to check margin:", symbols)# estimate profit for buying and sellinglot=1.0distance=300forsymbolinsymbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continuepoint=mt5.symbol_info(symbol).pointsymbol_tick=mt5.symbol_info_tick(symbol)ask=symbol_tick.askbid=symbol_tick.bidbuy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)ifbuy_profit!=None:print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)ifsell_profit!=None:print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())print()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')buy EURUSD 1.0 lot: profit on 300 points => 300.0 USDsell EURUSD 1.0 lot: profit on 300 points => 300.0 USDbuy GBPUSD 1.0 lot: profit on 300 points => 300.0 USDsell GBPUSD 1.0 lot: profit on 300 points => 300.0 USDbuy USDJPY 1.0 lot: profit on 300 points => 276.54 USDsell USDJPY 1.0 lot: profit on 300 points => 278.09 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols = ("EURUSD","GBPUSD","USDJPY")print("Symbols to check margin:", symbols)# estimate profit for buying and sellinglot=1.0distance=300forsymbolinsymbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continuepoint=mt5.symbol_info(symbol).pointsymbol_tick=mt5.symbol_info_tick(symbol)ask=symbol_tick.askbid=symbol_tick.bidbuy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)ifbuy_profit!=None:print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)ifsell_profit!=None:print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())print()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')buy EURUSD 1.0 lot: profit on 300 points => 300.0 USDsell EURUSD 1.0 lot: profit on 300 points => 300.0 USDbuy GBPUSD 1.0 lot: profit on 300 points => 300.0 USDsell GBPUSD 1.0 lot: profit on 300 points => 300.0 USDbuy USDJPY 1.0 lot: profit on 300 points => 276.54 USDsell USDJPY 1.0 lot: profit on 300 points => 278.09 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols = ("EURUSD","GBPUSD","USDJPY")print("Symbols to check margin:", symbols)# estimate profit for buying and sellinglot=1.0distance=300forsymbolinsymbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continuepoint=mt5.symbol_info(symbol).pointsymbol_tick=mt5.symbol_info_tick(symbol)ask=symbol_tick.askbid=symbol_tick.bidbuy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)ifbuy_profit!=None:print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)ifsell_profit!=None:print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())print()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')buy EURUSD 1.0 lot: profit on 300 points => 300.0 USDsell EURUSD 1.0 lot: profit on 300 points => 300.0 USDbuy GBPUSD 1.0 lot: profit on 300 points => 300.0 USDsell GBPUSD 1.0 lot: profit on 300 points => 300.0 USDbuy USDJPY 1.0 lot: profit on 300 points => 276.54 USDsell USDJPY 1.0 lot: profit on 300 points => 278.09 USD
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get account currencyaccount_currency=mt5.account_info().currencyprint("Account currency:",account_currency)# arrange the symbol listsymbols = ("EURUSD","GBPUSD","USDJPY")print("Symbols to check margin:", symbols)# estimate profit for buying and sellinglot=1.0distance=300forsymbolinsymbols:symbol_info=mt5.symbol_info(symbol)ifsymbol_info isNone:print(symbol,"not found, skipped")continueifnotsymbol_info.visible:print(symbol,"is not visible, trying to switch on")ifnotmt5.symbol_select(symbol,True):print("symbol_select({}}) failed, skipped",symbol)continuepoint=mt5.symbol_info(symbol).pointsymbol_tick=mt5.symbol_info_tick(symbol)ask=symbol_tick.askbid=symbol_tick.bidbuy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)ifbuy_profit!=None:print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)ifsell_profit!=None:print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));else:print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())print()# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29Account currency: USDSymbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')buy EURUSD 1.0 lot: profit on 300 points => 300.0 USDsell EURUSD 1.0 lot: profit on 300 points => 300.0 USDbuy GBPUSD 1.0 lot: profit on 300 points => 300.0 USDsell GBPUSD 1.0 lot: profit on 300 points => 300.0 USDbuy USDJPY 1.0 lot: profit on 300 points => 276.54 USDsell USDJPY 1.0 lot: profit on 300 points => 278.09 USD
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get account currency
account_currency=
mt5.account_info()
.currency
print
(
"Account currency:"
,account_currency)
# arrange the symbol list
symbols = (
"EURUSD"
,
"GBPUSD"
,
"USDJPY"
)
print
(
"Symbols to check margin:"
, symbols)
# estimate profit for buying and selling
lot=1.0
distance=300
for
symbol
in
symbols:
symbol_info=
mt5.symbol_info
(symbol)
if
symbol_info is
None
:
print
(symbol,
"not found, skipped"
)
continue
if
not
symbol_info.visible:
print
(symbol,
"is not visible, trying to switch on"
)
if
not
mt5.symbol_select
(symbol,
True
):
print
(
"symbol_select({}}) failed, skipped"
,symbol)
continue
point=
mt5.symbol_info
(symbol).point
symbol_tick=
mt5.symbol_info_tick
(symbol)
ask=symbol_tick.ask
bid=symbol_tick.bid
buy_profit=
mt5.order_calc_profit
(
mt5.ORDER_TYPE_BUY
,symbol,lot,ask,ask+distance*point)
if
buy_profit!=
None
:
print
(
"   buy {} {} lot: profit on {} points => {} {}"
.format(symbol,lot,distance,buy_profit,account_currency));
else
:
print
(
"order_calc_profit(ORDER_TYPE_BUY) failed, error code =",
mt5.last_error()
)
sell_profit=
mt5.order_calc_profit
(
mt5.ORDER_TYPE_SELL
,symbol,lot,bid,bid-distance*point)
if
sell_profit!=
None
:
print
(
"   sell {} {} lots: profit on {} points => {} {}"
.format(symbol,lot,distance,sell_profit,account_currency));
else
:
print
(
"order_calc_profit(ORDER_TYPE_SELL) failed, error code =",
mt5.last_error()
)
print
()
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
Account currency: USD
Symbols to check margin: ('EURUSD', 'GBPUSD', 'USDJPY')
buy EURUSD 1.0 lot: profit on 300 points => 300.0 USD
sell EURUSD 1.0 lot: profit on 300 points => 300.0 USD
buy GBPUSD 1.0 lot: profit on 300 points => 300.0 USD
sell GBPUSD 1.0 lot: profit on 300 points => 300.0 USD
buy USDJPY 1.0 lot: profit on 300 points => 276.54 USD
sell USDJPY 1.0 lot: profit on 300 points => 278.09 USD

---

## order_check

Check funds sufficiency for performing a requiredtrading operation. Check result are returned as theMqlTradeCheckResultstructure.

**Parameters**

request
request
[in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below.
[in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below.

**Return Value**

Check result as theMqlTradeCheckResultstructure. Therequestfield in the answer contains the structure of a trading request passed to order_check().
Check result as the
MqlTradeCheckResultstructure. The
request
field in the answer contains the structure of a trading request passed to order_check().

---

## order_send

Send arequestto perform atrading operationfrom the terminal to the trade server. The functionis similar toOrderSend.

**Parameters**

request
request
[in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below.
[in]MqlTradeRequesttype structure describing a required trading action. Required unnamed parameter. Example of filling in a request and the enumeration content are described below.

**Return Value**

Execution result as theMqlTradeResultstructure. Therequestfield in the answer contains the structure of a trading request passed to order_send().The info on the error can be obtained usinglast_error().
Execution result as the
MqlTradeResultstructure. The
request
field in the answer contains the structure of a trading request passed to order_send().
The info on the error can be obtained usinglast_error().
TheMqlTradeRequesttrading request structure
The
MqlTradeRequest
trading request structure
FieldDescriptionactionTrading operation type. The value can be one of the values of theTRADE_REQUEST_ACTIONSenumerationmagicEA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading requestorderOrder ticket. Required for modifying pending orderssymbolThe name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positionsvolumeRequested volume of a deal in lots. A real volume when making a deal depends on anorder execution type.pricePrice at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" (SYMBOL_TRADE_EXECUTION_MARKET) type having theTRADE_ACTION_DEALtypestoplimitA price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that momentslA price a Stop Loss order is activated at when the price moves in an unfavorable directiontpA price a Take Profit order is activated at when the price moves in a favorable directiondeviationMaximum acceptable deviation from the requested price, specified inpointstypeOrder type. The value can be one of the values of theORDER_TYPEenumerationtype_fillingOrder filling type. The value can be one of theORDER_TYPE_FILLINGvaluestype_timeOrder type by expiration. The value can be one of theORDER_TYPE_TIMEvaluesexpirationPending order expiration time (forTIME_SPECIFIEDtype orders)commentComment to an orderpositionPosition ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.position_byOpposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).
Field  Description
action  Trading operation type. The value can be one of the values of theTRADE_REQUEST_ACTIONSenumeration
magic  EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request
order  Order ticket. Required for modifying pending orders
symbol  The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions
volume  Requested volume of a deal in lots. A real volume when making a deal depends on anorder execution type.
price  Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" (SYMBOL_TRADE_EXECUTION_MARKET) type having theTRADE_ACTION_DEALtype
stoplimit  A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment
sl  A price a Stop Loss order is activated at when the price moves in an unfavorable direction
tp  A price a Take Profit order is activated at when the price moves in a favorable direction
deviation  Maximum acceptable deviation from the requested price, specified inpoints
type  Order type. The value can be one of the values of theORDER_TYPEenumeration
type_filling  Order filling type. The value can be one of theORDER_TYPE_FILLINGvalues
type_time  Order type by expiration. The value can be one of theORDER_TYPE_TIMEvalues
expiration  Pending order expiration time (forTIME_SPECIFIEDtype orders)
comment  Comment to an order
position  Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.
position_by  Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).
Field
Field
Field
Description
Description
Description
action
action
action
Trading operation type. The value can be one of the values of theTRADE_REQUEST_ACTIONSenumeration
Trading operation type. The value can be one of the values of theTRADE_REQUEST_ACTIONSenumeration
Trading operation type. The value can be one of the values of the
TRADE_REQUEST_ACTIONS
enumeration
magic
magic
magic
EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request
EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request
EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request
order
order
order
Order ticket. Required for modifying pending orders
Order ticket. Required for modifying pending orders
Order ticket. Required for modifying pending orders
symbol
symbol
symbol
The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions
The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions
The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions
volume
volume
volume
Requested volume of a deal in lots. A real volume when making a deal depends on anorder execution type.
Requested volume of a deal in lots. A real volume when making a deal depends on anorder execution type.
Requested volume of a deal in lots. A real volume when making a deal depends on an
order execution type
.
price
price
price
Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" (SYMBOL_TRADE_EXECUTION_MARKET) type having theTRADE_ACTION_DEALtype
Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" (SYMBOL_TRADE_EXECUTION_MARKET) type having theTRADE_ACTION_DEALtype
Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" (SYMBOL_TRADE_EXECUTION_MARKET) type having the
TRADE_ACTION_DEAL
type
stoplimit
stoplimit
stoplimit
A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment
A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment
A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment
sl
sl
sl
A price a Stop Loss order is activated at when the price moves in an unfavorable direction
A price a Stop Loss order is activated at when the price moves in an unfavorable direction
A price a Stop Loss order is activated at when the price moves in an unfavorable direction
tp
tp
tp
A price a Take Profit order is activated at when the price moves in a favorable direction
A price a Take Profit order is activated at when the price moves in a favorable direction
A price a Take Profit order is activated at when the price moves in a favorable direction
deviation
deviation
deviation
Maximum acceptable deviation from the requested price, specified inpoints
Maximum acceptable deviation from the requested price, specified inpoints
Maximum acceptable deviation from the requested price, specified in
points
type
type
type
Order type. The value can be one of the values of theORDER_TYPEenumeration
Order type. The value can be one of the values of theORDER_TYPEenumeration
Order type. The value can be one of the values of the
ORDER_TYPE
enumeration
type_filling
type_filling
type_filling
Order filling type. The value can be one of theORDER_TYPE_FILLINGvalues
Order filling type. The value can be one of theORDER_TYPE_FILLINGvalues
Order filling type. The value can be one of the
ORDER_TYPE_FILLING
values
type_time
type_time
type_time
Order type by expiration. The value can be one of theORDER_TYPE_TIMEvalues
Order type by expiration. The value can be one of theORDER_TYPE_TIMEvalues
Order type by expiration. The value can be one of the
ORDER_TYPE_TIME
values
expiration
expiration
expiration
Pending order expiration time (forTIME_SPECIFIEDtype orders)
Pending order expiration time (forTIME_SPECIFIEDtype orders)
Pending order expiration time (for
TIME_SPECIFIED
type orders)
comment
comment
comment
Comment to an order
Comment to an order
Comment to an order
position
position
position
Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.
Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.
Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.
position_by
position_by
position_by
Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).
Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).
Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).

---

## positions_total

Get the number of open positions.

**Return Value**

Integer value.
Integer value.

**Example**

importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of open positionspositions_total=mt5.positions_total()ifpositions_total>0:print("Total positions=",positions_total)else:print("Positions not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of open positionspositions_total=mt5.positions_total()ifpositions_total>0:print("Total positions=",positions_total)else:print("Positions not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of open positionspositions_total=mt5.positions_total()ifpositions_total>0:print("Total positions=",positions_total)else:print("Positions not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
importMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# check the presence of open positionspositions_total=mt5.positions_total()ifpositions_total>0:print("Total positions=",positions_total)else:print("Positions not found")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# check the presence of open positions
positions_total
=
mt5.positions_total
()
if
positions_total>0
:
print
(
"Total positions=",
positions_total
)
else
:
print
(
"Positions not found"
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## positions_get

Get open positions with the ability to filter by symbol or ticket. There are three call options.

**Parameters**

symbol="SYMBOL"
symbol="SYMBOL"
[in]  Symbol name. Optional named parameter. If a symbol is specified, theticketparameter is ignored.
[in]  Symbol name. Optional named parameter. If a symbol is specified, the
ticket
parameter is ignored.
group="GROUP"
group="GROUP"
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only positions meeting a specified criteria for a symbol name.
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only positions meeting a specified criteria for a symbol name.
ticket=TICKET
ticket=TICKET
[in]  Position ticket (POSITION_TICKET). Optional named parameter.
[in]  Position ticket (POSITION_TICKET). Optional named parameter.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get open positions on USDCHFpositions=mt5.positions_get(symbol="USDCHF")ifpositions==None:print("No positions on USDCHF, error code={}".format(mt5.last_error()))elif len(positions)>0:print("Total positions on USDCHF =",len(positions))# display all open positionsforpositioninpositions:print(position)# get the list of positions on symbols whose names contain "*USD*"usd_positions=mt5.positions_get(group="*USD*")ifusd_positions==None:print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))elif len(usd_positions)>0:print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))# display these positions as a table using pandas.DataFramedf=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29positions_get(group="*USD*")=5ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get open positions on USDCHFpositions=mt5.positions_get(symbol="USDCHF")ifpositions==None:print("No positions on USDCHF, error code={}".format(mt5.last_error()))elif len(positions)>0:print("Total positions on USDCHF =",len(positions))# display all open positionsforpositioninpositions:print(position)# get the list of positions on symbols whose names contain "*USD*"usd_positions=mt5.positions_get(group="*USD*")ifusd_positions==None:print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))elif len(usd_positions)>0:print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))# display these positions as a table using pandas.DataFramedf=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29positions_get(group="*USD*")=5ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get open positions on USDCHFpositions=mt5.positions_get(symbol="USDCHF")ifpositions==None:print("No positions on USDCHF, error code={}".format(mt5.last_error()))elif len(positions)>0:print("Total positions on USDCHF =",len(positions))# display all open positionsforpositioninpositions:print(position)# get the list of positions on symbols whose names contain "*USD*"usd_positions=mt5.positions_get(group="*USD*")ifusd_positions==None:print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))elif len(usd_positions)>0:print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))# display these positions as a table using pandas.DataFramedf=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29positions_get(group="*USD*")=5ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD
importMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get open positions on USDCHFpositions=mt5.positions_get(symbol="USDCHF")ifpositions==None:print("No positions on USDCHF, error code={}".format(mt5.last_error()))elif len(positions)>0:print("Total positions on USDCHF =",len(positions))# display all open positionsforpositioninpositions:print(position)# get the list of positions on symbols whose names contain "*USD*"usd_positions=mt5.positions_get(group="*USD*")ifusd_positions==None:print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))elif len(usd_positions)>0:print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))# display these positions as a table using pandas.DataFramedf=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29positions_get(group="*USD*")=5ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD
import
MetaTrader5
as
mt5
import
pandas
as
pd
pd
.
set_option
(
'display.max_columns'
,
500
)
# number of columns to be displayed
pd
.
set_option
(
'display.width', 1500
)
# max table width to display
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
()
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get open positions on USDCHF
positions
=
mt5.positions_get
(
symbol=
"USDCHF"
)
if
positions
==
None
:
print
(
"No positions on USDCHF, error code={}"
.format(
mt5.last_error()
))
elif len
(positions)>0
:
print
(
"Total positions on USDCHF =",
len
(positions)
)
# display all open positions
for
position
in
positions
:
print
(
position
)
# get the list of positions on symbols whose names contain "*USD*"
usd_positions
=
mt5.positions_get
(
group=
"*USD*"
)
if
usd_positions
==
None
:
print
(
"No positions with group=\"*USD*\", error code={}"
.
format
(
mt5.last_error()
))
elif len
(usd_positions)>0
:
print
(
"positions_get(group=\"*USD*\")={}"
.
format
(
len
(usd_positions)
))
# display these positions as a table using pandas.DataFrame
df=
pd.DataFrame
(
list
(
usd_positions
),columns=
usd_positions
[0]._asdict().keys())
df[
'time'
] = pd.to_datetime(df[
'time'
], unit='s')
df.drop([
'time_update', 'time_msc', 'time_update_msc', 'external_id'
], axis=1, inplace=True)
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
positions_get(group="*USD*")=5
ticket                time  type  magic  identifier  reason  volume  price_open       sl       tp  price_current  swap  profit  symbol comment
0  548297723 2020-03-18 15:00:55     1      0   548297723       3    0.01     1.09301  1.11490  1.06236        1.10104 -0.10   -8.03  EURUSD
1  548655158 2020-03-18 20:31:26     0      0   548655158       3    0.01     1.08676  1.06107  1.12446        1.10099 -0.08   14.23  EURUSD
2  548663803 2020-03-18 20:40:04     0      0   548663803       3    0.01     1.08640  1.06351  1.11833        1.10099 -0.08   14.59  EURUSD
3  548847168 2020-03-19 01:10:05     0      0   548847168       3    0.01     1.09545  1.05524  1.15122        1.10099 -0.06    5.54  EURUSD
4  548847194 2020-03-19 01:10:07     0      0   548847194       3    0.02     1.09536  1.04478  1.16587        1.10099 -0.08   11.26  EURUSD

---

## history_orders_total

Get the number of orders in trading history within the specified interval.

**Parameters**

date_from
date_from
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
date_to
date_to
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

**Return Value**

Integer value.
Integer value.

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_total(from_date, datetime.now())ifhistory_orders>0:print("Total history orders=",history_orders)else:print("Orders not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_total(from_date, datetime.now())ifhistory_orders>0:print("Total history orders=",history_orders)else:print("Orders not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_total(from_date, datetime.now())ifhistory_orders>0:print("Total history orders=",history_orders)else:print("Orders not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_total(from_date, datetime.now())ifhistory_orders>0:print("Total history orders=",history_orders)else:print("Orders not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get the number of orders in history
from_date
=
datetime
(
2020
,
1
,
1
)
to_date
=
datetime
.
now
()
history_orders
=
mt5.history_orders_total
(
from_date
, datetime.now())
if
history_orders>0
:
print
(
"Total history orders=",
history_orders
)
else
:
print
(
"Orders not found in history"
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## history_orders_get

Get orders from trading history with the ability to filter by ticket or position. There are three call options.

**Parameters**

date_from
date_from
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
date_to
date_to
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
group="GROUP"
group="GROUP"
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name.
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only orders meeting a specified criteria for a symbol name.
ticket=TICKET
ticket=TICKET
[in]  Order ticket that should be received. Optional parameter. If not specified, the filter is not applied.
[in]  Order ticket that should be received. Optional parameter. If not specified, the filter is not applied.
position=POSITION
position=POSITION
[in]  Ticket of a position (stored inORDER_POSITION_ID) all orders should be received for. Optional parameter. If not specified, the filter is not applied.
[in]  Ticket of a position (stored in
ORDER_POSITION_ID
) all orders should be received for. Optional parameter. If not specified, the filter is not applied.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")ifhistory_orders==None:print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))elif len(history_orders)>0:print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))print()# display all historical orders by a position ticketposition_id=530218319position_history_orders=mt5.history_orders_get(position=position_id)ifposition_history_orders==None:print("No orders with position #{}".format(position_id))print("error code =",mt5.last_error())elif len(position_history_orders)>0:print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))# display all historical orders having a specified position ticketforposition_orderinposition_history_orders:print(position_order)print()# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')df['time_done'] = pd.to_datetime(df['time_done'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14Total history orders on position #530218319: 2TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF
fromdatetimeimportdatetimeimportMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")ifhistory_orders==None:print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))elif len(history_orders)>0:print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))print()# display all historical orders by a position ticketposition_id=530218319position_history_orders=mt5.history_orders_get(position=position_id)ifposition_history_orders==None:print("No orders with position #{}".format(position_id))print("error code =",mt5.last_error())elif len(position_history_orders)>0:print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))# display all historical orders having a specified position ticketforposition_orderinposition_history_orders:print(position_order)print()# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')df['time_done'] = pd.to_datetime(df['time_done'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14Total history orders on position #530218319: 2TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF
fromdatetimeimportdatetimeimportMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")ifhistory_orders==None:print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))elif len(history_orders)>0:print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))print()# display all historical orders by a position ticketposition_id=530218319position_history_orders=mt5.history_orders_get(position=position_id)ifposition_history_orders==None:print("No orders with position #{}".format(position_id))print("error code =",mt5.last_error())elif len(position_history_orders)>0:print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))# display all historical orders having a specified position ticketforposition_orderinposition_history_orders:print(position_order)print()# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')df['time_done'] = pd.to_datetime(df['time_done'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14Total history orders on position #530218319: 2TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF
fromdatetimeimportdatetimeimportMetaTrader5asmt5importpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of orders in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")ifhistory_orders==None:print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))elif len(history_orders)>0:print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))print()# display all historical orders by a position ticketposition_id=530218319position_history_orders=mt5.history_orders_get(position=position_id)ifposition_history_orders==None:print("No orders with position #{}".format(position_id))print("error code =",mt5.last_error())elif len(position_history_orders)>0:print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))# display all historical orders having a specified position ticketforposition_orderinposition_history_orders:print(position_order)print()# display these orders as a table using pandas.DataFramedf=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')df['time_done'] = pd.to_datetime(df['time_done'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14Total history orders on position #530218319: 2TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF
from
datetime
import
datetime
import
MetaTrader5
as
mt5
import
pandas
as
pd
pd
.
set_option
(
'display.max_columns'
,
500
)
# number of columns to be displayed
pd
.
set_option
(
'display.width', 1500
)
# max table width to display
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
()
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get the number of orders in history
from_date
=
datetime
(
2020
,
1
,
1
)
to_date
=
datetime
.
now
()
history_orders
=
mt5.history_orders_get
(
from_date
, to_date
, group=
"*GBP*"
)
if
history_orders
==
None
:
print
(
"No history orders with group=\"*GBP*\", error code={}"
.
format
(
mt5.last_error()
))
elif len
(history_orders)>0
:
print
(
"history_orders_get({}, {}, group=\"*GBP*\")={}"
.
format
(from_date,to_date,
len
(history_orders)
))
print
()
# display all historical orders by a position ticket
position_id=530218319
position_history_orders
=
mt5.history_orders_get
(position=
position_id
)
if
position_history_orders==
None
:
print
(
"No orders with position #{}"
.format(
position_id
))
print
(
"error code ="
,
mt5.last_error()
)
elif len
(position_history_orders)>0
:
print
(
"Total history orders on position #{}: {}"
.
format
(position_id,
len
(position_history_orders)
))
# display all historical orders having a specified position ticket
for
position_order
in
position_history_orders
:
print
(
position_order
)
print
()
# display these orders as a table using pandas.DataFrame
df=
pd.DataFrame
(
list
(position_history_orders),columns=position_history_orders[0]._asdict().keys())
df.drop([
'time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'
], axis=1, inplace=
True
)
df[
'time_setup'
] = pd.to_datetime(df[
'time_setup'
], unit='s')
df[
'time_done'
] = pd.to_datetime(df[
'time_done'
], unit='s')
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
history_orders_get(2020-01-01 00:00:00, 2020-03-25 17:17:32.058795, group="*GBP*")=14
Total history orders on position #530218319: 2
TradeOrder(ticket=530218319, time_setup=1582282114, time_setup_msc=1582282114681, time_done=1582303777, time_done_msc=1582303777582, time_expiration=0, ...
TradeOrder(ticket=535548147, time_setup=1583176242, time_setup_msc=1583176242265, time_done=1583176242, time_done_msc=1583176242265, time_expiration=0, ...
ticket          time_setup  time_setup_msc           time_done  time_done_msc  type  type_filling  magic  position_id  volume_initial  price_open  price_current  symbol comment external_id
0  530218319 2020-02-21 10:48:34   1582282114681 2020-02-21 16:49:37  1582303777582     2             2      0    530218319            0.01     0.97898        0.97863  USDCHF
1  535548147 2020-03-02 19:10:42   1583176242265 2020-03-02 19:10:42  1583176242265     1             0      0    530218319            0.01     0.95758        0.95758  USDCHF

---

## history_deals_total

Get the number of deals in trading history within the specified interval.

**Parameters**

date_from
date_from
[in]  Date the deals are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date the deals are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
date_to
date_to
[in]  Date, up to which the deals are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.
[in]  Date, up to which the deals are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter.

**Return Value**

Integer value.
Integer value.

**Example**

fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()deals=mt5.history_deals_total(from_date,to_date)ifdeals>0:print("Total deals=",deals)else:print("Deals not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()deals=mt5.history_deals_total(from_date,to_date)ifdeals>0:print("Total deals=",deals)else:print("Deals not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()deals=mt5.history_deals_total(from_date,to_date)ifdeals>0:print("Total deals=",deals)else:print("Deals not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
fromdatetimeimportdatetimeimportMetaTrader5asmt5# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)# establish connection to MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()deals=mt5.history_deals_total(from_date,to_date)ifdeals>0:print("Total deals=",deals)else:print("Deals not found in history")# shut down connection to the MetaTrader 5 terminalmt5.shutdown()
from
datetime
import
datetime
import
MetaTrader5
as
mt5
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
# establish connection to MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get the number of deals in history
from_date
=
datetime
(
2020
,
1
,
1
)
to_date
=
datetime
.
now
()
deals
=
mt5.history_deals_total
(
from_date
,
to_date
)
if
deals>0
:
print
(
"Total deals=",
deals
)
else
:
print
(
"Deals not found in history"
)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()

---

## history_deals_get

Get deals from trading history within the specified interval with the ability to filter by ticket or position.

**Parameters**

date_from
date_from
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
[in]  Date the orders are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified first.
date_to
date_to
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
[in]  Date, up to which the orders are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter is specified second.
group="GROUP"
group="GROUP"
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name.
[in]  The filter for arranging a group of necessary symbols. Optional named parameter. If the group is specified, the function returns only deals meeting a specified criteria for a symbol name.
ticket=TICKET
ticket=TICKET
[in]  Ticket of an order (stored inDEAL_ORDER) all deals should be received for. Optional parameter. If not specified, the filter is not applied.
[in]  Ticket of an order (stored in
DEAL_ORDER
) all deals should be received for. Optional parameter. If not specified, the filter is not applied.
position=POSITION
position=POSITION
[in]  Ticket of a position (stored inDEAL_POSITION_ID) all deals should be received for. Optional parameter. If not specified, the filter is not applied.
[in]  Ticket of a position (stored in
DEAL_POSITION_ID
) all deals should be received for. Optional parameter. If not specified, the filter is not applied.

**Return Value**

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().
Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained usinglast_error().

**Example**

importMetaTrader5asmt5fromdatetimeimportdatetimeimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()# get deals for symbols whose names contain "GBP" within a specified intervaldeals=mt5.history_deals_get(from_date,to_date, group="*GBP*")ifdeals==None:print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))eliflen(deals)> 0:print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))# get deals for symbols whose names contain neither "EUR" nor "GBP"deals =mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")ifdeals ==None:print("No deals, error code={}".format(mt5.last_error()))eliflen(deals) > 0:print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =",len(deals))# display all obtained deals 'as is'fordealindeals:print("  ",deal)print()# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)print("")# get all deals related to the position #530218319position_id=530218319position_deals =mt5.history_deals_get(position=position_id)ifposition_deals ==None:print("No deals with position #{}".format(position_id))print("error code =",mt5.last_error())eliflen(position_deals) > 0:print("Deals with position id #{}: {}".format(position_id,len(position_deals)))# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_deals_get(from_date, to_date, group="*GBP*") = 14history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.01  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSDDeals with position id #530218319: 2ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF
importMetaTrader5asmt5fromdatetimeimportdatetimeimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()# get deals for symbols whose names contain "GBP" within a specified intervaldeals=mt5.history_deals_get(from_date,to_date, group="*GBP*")ifdeals==None:print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))eliflen(deals)> 0:print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))# get deals for symbols whose names contain neither "EUR" nor "GBP"deals =mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")ifdeals ==None:print("No deals, error code={}".format(mt5.last_error()))eliflen(deals) > 0:print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =",len(deals))# display all obtained deals 'as is'fordealindeals:print("  ",deal)print()# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)print("")# get all deals related to the position #530218319position_id=530218319position_deals =mt5.history_deals_get(position=position_id)ifposition_deals ==None:print("No deals with position #{}".format(position_id))print("error code =",mt5.last_error())eliflen(position_deals) > 0:print("Deals with position id #{}: {}".format(position_id,len(position_deals)))# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_deals_get(from_date, to_date, group="*GBP*") = 14history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.01  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSDDeals with position id #530218319: 2ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF
importMetaTrader5asmt5fromdatetimeimportdatetimeimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()# get deals for symbols whose names contain "GBP" within a specified intervaldeals=mt5.history_deals_get(from_date,to_date, group="*GBP*")ifdeals==None:print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))eliflen(deals)> 0:print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))# get deals for symbols whose names contain neither "EUR" nor "GBP"deals =mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")ifdeals ==None:print("No deals, error code={}".format(mt5.last_error()))eliflen(deals) > 0:print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =",len(deals))# display all obtained deals 'as is'fordealindeals:print("  ",deal)print()# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)print("")# get all deals related to the position #530218319position_id=530218319position_deals =mt5.history_deals_get(position=position_id)ifposition_deals ==None:print("No deals with position #{}".format(position_id))print("error code =",mt5.last_error())eliflen(position_deals) > 0:print("Deals with position id #{}: {}".format(position_id,len(position_deals)))# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_deals_get(from_date, to_date, group="*GBP*") = 14history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.01  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSDDeals with position id #530218319: 2ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF
importMetaTrader5asmt5fromdatetimeimportdatetimeimportpandasaspdpd.set_option('display.max_columns',500)# number of columns to be displayedpd.set_option('display.width', 1500)# max table width to display# display data on the MetaTrader 5 packageprint("MetaTrader5 package author: ",mt5.__author__)print("MetaTrader5 package version: ",mt5.__version__)print()# establish connection to the MetaTrader 5 terminalif notmt5.initialize():print("initialize() failed, error code =",mt5.last_error())quit()# get the number of deals in historyfrom_date=datetime(2020,1,1)to_date=datetime.now()# get deals for symbols whose names contain "GBP" within a specified intervaldeals=mt5.history_deals_get(from_date,to_date, group="*GBP*")ifdeals==None:print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))eliflen(deals)> 0:print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))# get deals for symbols whose names contain neither "EUR" nor "GBP"deals =mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")ifdeals ==None:print("No deals, error code={}".format(mt5.last_error()))eliflen(deals) > 0:print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =",len(deals))# display all obtained deals 'as is'fordealindeals:print("  ",deal)print()# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)print("")# get all deals related to the position #530218319position_id=530218319position_deals =mt5.history_deals_get(position=position_id)ifposition_deals ==None:print("No deals with position #{}".format(position_id))print("error code =",mt5.last_error())eliflen(position_deals) > 0:print("Deals with position id #{}: {}".format(position_id,len(position_deals)))# display these deals as a table using pandas.DataFramedf=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())df['time'] = pd.to_datetime(df['time'], unit='s')print(df)# shut down connection to the MetaTrader 5 terminalmt5.shutdown()Result:MetaTrader5 package author:  MetaQuotes Software Corp.MetaTrader5 package version:  5.0.29history_deals_get(from_date, to_date, group="*GBP*") = 14history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.01  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSDDeals with position id #530218319: 2ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF
import
MetaTrader5
as
mt5
from
datetime
import
datetime
import
pandas
as
pd
pd
.
set_option
(
'display.max_columns'
,
500
)
# number of columns to be displayed
pd
.
set_option
(
'display.width', 1500
)
# max table width to display
# display data on the MetaTrader 5 package
print
(
"MetaTrader5 package author: "
,
mt5.__author__
)
print
(
"MetaTrader5 package version: "
,
mt5.__version__
)
print
()
# establish connection to the MetaTrader 5 terminal
if not
mt5.initialize
():
print
(
"initialize() failed, error code ="
,
mt5.last_error()
)
quit()
# get the number of deals in history
from_date
=
datetime
(
2020
,
1
,
1
)
to_date
=
datetime
.
now
()
# get deals for symbols whose names contain "GBP" within a specified interval
deals
=
mt5.history_deals_get
(
from_date
,
to_date, group=
"*GBP*"
)
if
deals
==
None
:
print
(
"No deals with group=\"*USD*\", error code={}"
.format(
mt5.last_error()
))
elif
len
(deals)> 0:
print
(
"history_deals_get({}, {}, group=\"*GBP*\")={}"
.
format
(from_date,to_date,
len
(deals)))
# get deals for symbols whose names contain neither "EUR" nor "GBP"
deals =
mt5.history_deals_get
(from_date, to_date, group=
"*,!*EUR*,!*GBP*"
)
if
deals ==
None
:
print
(
"No deals, error code={}"
.
format
(
mt5.last_error()
))
elif
len
(deals) > 0:
print
(
"history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") ="
,
len
(deals))
# display all obtained deals 'as is'
for
deal
in
deals:
print
(
"  "
,deal)
print
()
# display these deals as a table using pandas.DataFrame
df=
pd.DataFrame
(
list
(deals),columns=deals[0]._asdict().keys())
df[
'time'
] = pd.to_datetime(df[
'time'
], unit='s')
print
(df)
print
("")
# get all deals related to the position #530218319
position_id=530218319
position_deals =
mt5.history_deals_get
(position=position_id)
if
position_deals ==
None
:
print
(
"No deals with position #{}"
.
format
(position_id))
print
(
"error code ="
,
mt5.last_error()
)
elif
len
(position_deals) > 0:
print(
"Deals with position id #{}: {}"
.
format
(position_id,
len
(position_deals)))
# display these deals as a table using pandas.DataFrame
df=
pd.DataFrame
(
list
(position_deals),columns=position_deals[0]._asdict().keys())
df[
'time'
] = pd.to_datetime(df[
'time'
], unit='s')
print
(df)
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown
()
Result:
MetaTrader5 package author:  MetaQuotes Software Corp.
MetaTrader5 package version:  5.0.29
history_deals_get(from_date, to_date, group="*GBP*") = 14
history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*") = 7
TradeDeal(ticket=506966741, order=0, time=1582202125, time_msc=1582202125419, type=2, entry=0, magic=0, position_id=0, reason=0, volume=0.0, pri ...
TradeDeal(ticket=507962919, order=530218319, time=1582303777, time_msc=1582303777582, type=0, entry=0, magic=0, position_id=530218319, reason=0, ...
TradeDeal(ticket=513149059, order=535548147, time=1583176242, time_msc=1583176242265, type=1, entry=1, magic=0, position_id=530218319, reason=0, ...
TradeDeal(ticket=516943494, order=539349382, time=1583510003, time_msc=1583510003895, type=1, entry=0, magic=0, position_id=539349382, reason=0, ...
TradeDeal(ticket=516943915, order=539349802, time=1583510025, time_msc=1583510025054, type=0, entry=0, magic=0, position_id=539349802, reason=0, ...
TradeDeal(ticket=517139682, order=539557870, time=1583520201, time_msc=1583520201227, type=0, entry=1, magic=0, position_id=539349382, reason=0, ...
TradeDeal(ticket=517139716, order=539557909, time=1583520202, time_msc=1583520202971, type=1, entry=1, magic=0, position_id=539349802, reason=0, ...
ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap     profit  fee  symbol comment external_id
0  506966741          0 2020-02-20 12:35:25  1582202125419     2      0      0            0       0    0.00  0.00000         0.0   0.0  100000.00  0.0
1  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0       0.00  0.0  USDCHF
2  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0     -22.35  0.0  USDCHF
3  516943494  539349382 2020-03-06 15:53:23  1583510003895     1      0      0    539349382       0    0.10  0.93475         0.0   0.0       0.00  0.0  USDCHF
4  516943915  539349802 2020-03-06 15:53:45  1583510025054     0      0      0    539349802       0    0.10  0.66336         0.0   0.0       0.00  0.0  AUDUSD
5  517139682  539557870 2020-03-06 18:43:21  1583520201227     0      1      0    539349382       0    0.10  0.93751         0.0   0.0     -29.44  0.0  USDCHF
6  517139716  539557909 2020-03-06 18:43:22  1583520202971     1      1      0    539349802       0    0.10  0.66327         0.0   0.0      -0.90  0.0  AUDUSD
Deals with position id #530218319: 2
ticket      order                time       time_msc  type  entry  magic  position_id  reason  volume    price  commission  swap  profit  fee  symbol comment external_id
0  507962919  530218319 2020-02-21 16:49:37  1582303777582     0      0      0    530218319       0    0.01  0.97898         0.0   0.0    0.00  0.0  USDCHF
1  513149059  535548147 2020-03-02 19:10:42  1583176242265     1      1      0    530218319       0    0.01  0.95758         0.0   0.0  -22.35  0.0  USDCHF

---
