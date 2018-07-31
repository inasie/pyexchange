# pyexchange
Python wrapper of cryptocurrency exchange pubilc APIs

## Supported exchanges
| Name | Version | URL |
|---|---|---|
| Bitflyer  | v1 | https://lightning.bitflyer.com/docs?lang=en |
| Binance  | v1 | https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md |
| Bitfinex  | v1 | https://bitfinex.readme.io/v1/reference |
| Bithumb  | Unknown | https://www.bithumb.com/u1/US127 |
| Coinone  | v.1.10 | https://doc.coinone.co.kr |
| Gopax  | Unknown | https://www.gopax.co.kr/API |
| Huobi  | v1 | https://github.com/huobiapi/API_Docs_en/wiki |
| OKEx  | v1 | https://github.com/okcoin-okex/API-docs-OKEx.com |
| Upbit  | v1.0 | https://docs.upbit.com/v1.0/reference |
| ZB  | v1 | https://www.zb.com/i/developer/restApi |

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