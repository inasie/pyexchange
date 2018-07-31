import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.hitbtc.hitbtc import HitBTC


class ExchangeHitBTC(ExchangeBase):
    """
    HitBTC
    """
    NAME = 'HitBTC'
    VERSION = '2'
    URL = 'https://api.hitbtc.com'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._hitbtc = HitBTC()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        symbols = self._hitbtc.get_symbols()

        for symbol_obj in symbols:
            market_currency = symbol_obj['quoteCurrency']
            currency = symbol_obj['baseCurrency']
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
        symbol = currency_pair.currency + currency_pair.market_currency
        ticker = self._hitbtc.get_ticker(symbol)

        price = float(ticker['last'])
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
        symbol = currency_pair.currency + currency_pair.market_currency

        orderbook = self._hitbtc.get_orderbook(symbol)

        asks = []
        for unit in orderbook['ask']:
            price = float(unit['price'])
            amount = float(unit['size'])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['bid']:
            price = float(unit['price'])
            amount = float(unit['size'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
