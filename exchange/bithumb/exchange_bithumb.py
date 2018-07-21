import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bithumb.bithumb import Bithumb


class ExchangeBithumb(ExchangeBase):
    """
    Bithumb
    """
    NAME = 'Bithumb'
    VERSION = '1.0'
    URL = 'https://www.bithumb.com/u1/US127'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.bithumb = Bithumb()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        ticker_all = self.bithumb.ticker('ALL')
        if int(ticker_all['status']) != 0:
            raise Exception('ticker() failed(%s)' % ticker_all['status'])
        for key in ticker_all['data'].keys():
            if key == 'date':
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
        ticker = self.bithumb.ticker(currency_pair.currency)
        if int(ticker['status']) != 0:
            raise Exception('ticker() failed(%s)' % ticker['status'])
        price = float(ticker['data']['closing_price'])
        timestamp = int(ticker['data']['date'])
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
        orderbook = self.bithumb.orderbook(currency_pair.currency)
        if int(orderbook['status']) != 0:
            raise Exception('orderbook() failed(%s)' % orderbook['status'])

        timestamp = orderbook['data']['timestamp']
        asks = []
        for unit in orderbook['data']['asks']:
            price = float(unit['price'])
            amount = float(unit['quantity'])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['data']['bids']:
            price = float(unit['price'])
            amount = float(unit['quantity'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
