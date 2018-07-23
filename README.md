# pyexchange
Python wrapper of cryptocurrency exchange pubilc APIs

## Exchanges
Currently supported - Bithumb, Upbit, Bitfinex, Binance <br>
TODO: OKEx, Huobi, ...

## API
### ExchangeAPI
| API  | Param  | Return | Description |
|---|---|---|--|
| get_exchanges | None | str[] | Currently supported exchanges |
| create_exchange | str | Exchange | create an Exchange obj |

### Exchange
| API  | Param  | Return | Description |
|---|---|---|---|
| get_currency_pairs | None | CurrenyPair[] | Gets currency list supported by exchange |
| get_ticker | CurrencyPair | Ticker | Gets last price |
| get_orderbook | CurrencyPair | Orderbook | Gets orderbook info |

## Example
```python
from exchange import CurrencyPair
from exchange import ExchangeAPI

binance = ExchangeAPI().create_exchange('Binance')
ticker = binance.get_ticker(CurrencyPair('USD', 'BTC'))
print(ticker)
```
Please refer unittest for more example codes