from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.binance.binance import Binance


class ExchangeBianace(ExchangeBase):
    """
    Binance
    """
    NAME = 'Binance'
    VERSION = 'v1'
    URL = 'https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.binance = Binance()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        exchange_info = self.binance.get_exchange_info()
        for symbol in exchange_info['symbols']:
            currency = symbol['baseAsset']
            market_currency = symbol['symbol'][len(currency):]
            currency_pairs.append(CurrencyPair(market_currency, currency))
        return currency_pairs

    def get_ticker(self, currency_pair):
        '''
        Gets last price
        :param CurrencyPair currency_pair: currency pair
        :return: ticker
        :rtype: Ticker
        '''
        if currency_pair is None:
            raise InvalidParamException('currency_pair is None')
        market_currency = currency_pair.market_currency
        currency = currency_pair.currency
        symbol = currency + market_currency

        price = float(self.binance.get_ticker_price(symbol)['price'])
        return Ticker(currency_pair, price)

    def get_orderbook(self, currency_pair):
        '''
        Gets orderbook information
        :param CurrencyPair currency_pair: currency pair
        :return: orderbook
        :rtype: Orderbook
        '''
        if currency_pair is None:
            raise InvalidParamException('currency_pair is None')
        market_currency = currency_pair.market_currency
        currency = currency_pair.currency
        symbol = currency + market_currency

        orderbook = self.binance.get_orderbook(symbol)
        asks = []
        for unit in orderbook['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
