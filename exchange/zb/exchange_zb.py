import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.zb.zb import ZB


class ExchangeZB(ExchangeBase):
    """
    ZB
    """
    NAME = 'ZB'
    VERSION = 'v1'
    URL = 'https://www.zb.com/i/developer/restApi'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._zb = ZB()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        markets = self._zb.get_markets()

        for market in markets.keys():
            market_currency = market.split('_')[1].upper()
            currency = market.split('_')[0].upper()
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
        market = currency_pair.currency + '_' + currency_pair.market_currency
        ticker = self._zb.get_ticker(market)

        timestamp = int(ticker['date'])
        price = float(ticker['ticker']['last'])
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
        market = currency_pair.currency + '_' + currency_pair.market_currency
        depth = self._zb.get_depth(market)

        timestamp = depth['timestamp']
        asks = []
        for unit in depth['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.insert(0, OrderbookItem(price, amount))

        bids = []
        for unit in depth['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
