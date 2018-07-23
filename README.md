# pyexchange
Python wrapper of cryptocurrency exchange pubilc APIs

## Supported exchanges
| Name | Version | URL |
|---|---|---|
| Binance  | v1 | https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md |
| Bitfinex  | v1 | https://bitfinex.readme.io/v1/reference |
| Bithumb  | Unknown | https://www.bithumb.com/u1/US127 |
| Upbit  | v1.0 | https://docs.upbit.com/v1.0/reference |

TODO: OKEx, Huobi, ...

## API
### ExchangeAPI
| API  | Param  | Return | Description |
|---|---|---|--|
| get_exchanges | None | str[] | Gets supported exchanges |
| create_exchange | str | Exchange | Creates an exchange object |

### Exchange
| API  | Param  | Return | Description |
|---|---|---|---|
| get_currency_pairs | None | CurrenyPair[] | Gets supported currency pair list |
| get_ticker | CurrencyPair | Ticker | Gets last price |
| get_orderbook | CurrencyPair | Orderbook | Gets orderbook |

## Example
```python
from exchange import CurrencyPair
from exchange import ExchangeAPI

binance = ExchangeAPI().create_exchange('Binance')
ticker = binance.get_ticker(CurrencyPair('USD', 'BTC'))
print(ticker)
```
Please refer unittest for more example codes