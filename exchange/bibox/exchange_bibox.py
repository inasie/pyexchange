import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bibox.bibox import Bibox


class ExchangeBibox(ExchangeBase):
    """
    Bibox
    """
    NAME = 'Bibox'
    VERSION = 'v1'
    URL = 'https://github.com/Biboxcom/api_reference/wiki/home_en'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._bibox = Bibox()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        pair_list = self._bibox.get_pair_list()

        for pair in pair_list['result']:
            market_currency = pair['pair'].split('_')[1]
            currency = pair['pair'].split('_')[0]
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
        pair = currency_pair.currency + '_' + currency_pair.market_currency
        ticker = self._bibox.get_ticker(pair)
        timestamp = int(ticker['result']['timestamp'])
        price = float(ticker['result']['last'])
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
        pair = currency_pair.currency + '_' + currency_pair.market_currency
        depth = self._bibox.get_depth(pair, size=50)

        timestamp = int(depth['result']['update_time'])
        asks = []
        for unit in depth['result']['asks']:
            price = float(unit['price'])
            amount = float(unit['volume'])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in depth['result']['bids']:
            price = float(unit['price'])
            amount = float(unit['volume'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
