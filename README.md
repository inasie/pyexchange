# pyexchange
Python wrapper of cryptocurrency exchange pubilc APIs

## Supported exchanges
| Name | Version | URL |
|---|---|---|
| Bibox  | v1 | https://github.com/Biboxcom/api_reference/wiki/home_en |
| Bitflyer  | v1 | https://lightning.bitflyer.com/docs?lang=en |
| Binance  | v1 | https://github.com/binance-exchange/binance-official-api-docs |
| Bitfinex  | v1 | https://bitfinex.readme.io/v1/reference |
| Bitforex  | v1 | https://github.com/bitforexapi/API_Doc_en |
| Bithumb  | Unknown | https://www.bithumb.com/u1/US127 |
| Coinbase Pro  | Unknown | https://docs.pro.coinbase.com |
| Coinbene | v1 | https://github.com/Coinbene/API-Documents/wiki/0.0.0-Coinbene-API-documents |
| CoinEx | v1 | https://github.com/coinexcom/coinex_exchange_api/wiki |
| Coinone  | v.1.10 | https://doc.coinone.co.kr |
| Gopax  | Unknown | https://www.gopax.co.kr/API |
| HitBTC  | 2 | https://api.hitbtc.com |
| Huobi  | v1 | https://github.com/huobiapi/API_Docs_en/wiki |
| LBank  | v1 | https://github.com/LBank-exchange/lbank-official-api-docs |
| OKEx  | v1 | https://github.com/okcoin-okex/API-docs-OKEx.com |
| Upbit  | v1.0 | https://docs.upbit.com/v1.0/reference |
| ZB | v1 | https://www.zb.com/i/developer/restApi |

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
for pair in binance.get_currency_pairs():
    print(pair)
# market_currency: BTC, currency: ETH
# market_currency: BTC, currency: LTC
# market_currency: BTC, currency: BNB
# market_currency: BTC, currency: NEO
# market_currency: ETH, currency: QTUM
# ...

print(binance.get_ticker(CurrencyPair('USDT', 'BTC')))
# currency_pair: market_currency: USDT, currency: BTC, price: 7505.27, timestamp: 1533219056

print(binance.get_orderbook(CurrencyPair('USDT', 'BTC')))
# Orderbook(1533219081)-(market_currency: USDT, currency: BTC)
# Bids -
#         price: 7504.00000, amount: 0.14538
#         price: 7502.00000, amount: 0.23498
#         price: 7501.00000, amount: 0.62473
#         price: 7500.38000, amount: 0.05693
#         price: 7500.06000, amount: 0.34357
# ...
# Bids -
#         price: 7504.00000, amount: 0.14538
#         price: 7502.00000, amount: 0.23498
#         price: 7501.00000, amount: 0.62473
#         price: 7500.38000, amount: 0.05693
#         price: 7500.06000, amount: 0.34357
# '''

```
Please refer unittest for more example codes

## Donate
|Cryptocurrency|Address|
|---|---|
|BTC|3LQ8rM139ehmGbqKwmKaEpiCyZhvGViLi8|
|BCH|34FczBgU3F4S9tympRncaZ9AAQTqkbFKDJ|
|ETH|0x3102857c163bc6ec97b358d877897a4bd9fcc556|
|QTUM|Qd9yEPh6KUcxTuz1k8MhWpmP44VnBkCsnD|
|ICON|hxdce20a7bf7437a0b5a062ea8d956a20460da7dc1|
