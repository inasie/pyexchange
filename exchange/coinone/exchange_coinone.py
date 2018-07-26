import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.coinone.coinone import Coinone


class ExchangeCoinone(ExchangeBase):
    """
    Coinone
    """
    NAME = 'Coinone'
    VERSION = 'v.1.10'
    URL = 'https://doc.coinone.co.kr'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._coinone = Coinone()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        ticker_all = self._coinone.get_ticker('all')

        for key in ticker_all.keys():
            if key in ['errorCode', 'result', 'timestamp']:
                continue
            currency_pairs.append(CurrencyPair("KRW", key.upper()))
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
        if currency_pair.base_currency != 'KRW':
            raise InvalidParamException('invalid base_currency')
        ticker = self._coinone.get_ticker(currency_pair.currency)
        price = float(ticker['last'])
        timestamp = int(ticker['timestamp'])
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
        if currency_pair.base_currency != 'KRW':
            raise InvalidParamException('invalid base_currency')
        orderbook = self._coinone.get_orderbook(currency_pair.currency)

        timestamp = int(orderbook['timestamp'])
        asks = []
        for unit in orderbook['ask']:
            price = float(unit['price'])
            amount = float(unit['qty'])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['bid']:
            price = float(unit['price'])
            amount = float(unit['qty'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
