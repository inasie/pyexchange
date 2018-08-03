import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.coinbene.coinbene import Coinbene


class ExchangeCoinbene(ExchangeBase):
    """
    Coinbene
    """
    NAME = 'Coinbene'
    VERSION = 'v1'
    URL = 'https://github.com/Coinbene/API-Documents/wiki/0.0.0-Coinbene-API-documents'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._bene = Coinbene()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        symbols = self._bene.get_symbols()

        for symbol in symbols['symbol']:
            market_currency = symbol['quoteAsset']
            currency = symbol['baseAsset']
            currency_pairs.append(
                CurrencyPair(market_currency, currency))
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
        ticker = self._bene.get_ticker(symbol)
        timestamp = int(ticker['timestamp'])
        price = float(ticker['ticker'][0]['last'])
        return Ticker(currency_pair, price, timestamp)

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
        orderbook = self._bene.get_orderbook(symbol, 50)

        timestamp = orderbook['timestamp']
        asks = []
        for unit in orderbook['orderbook']['asks']:
            price = float(unit['price'])
            amount = float(unit['quantity'])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['orderbook']['bids']:
            price = float(unit['price'])
            amount = float(unit['quantity'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
