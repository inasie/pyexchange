import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bitforex.bitforex import Bitforex


class ExchangeBitforex(ExchangeBase):
    """
    Bitforex
    """
    NAME = 'Bitforex'
    VERSION = 'v1'
    URL = 'https://github.com/bitforexapi/API_Doc_en'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._bf = Bitforex()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        symbols = self._bf.get_symbols()

        for symbol in symbols['data']:
            market_currency = symbol['symbol'].split('-')[1].upper()
            currency = symbol['symbol'].split('-')[2].upper()
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
        symbol = 'coin-%s-%s' % (currency_pair.market_currency.lower(),
                                 currency_pair.currency.lower())
        ticker = self._bf.get_ticker(symbol)
        timestamp = ticker['data']['date']
        price = float(ticker['data']['last'])
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
        symbol = 'coin-%s-%s' % (currency_pair.market_currency.lower(),
                                 currency_pair.currency.lower())
        depth = self._bf.get_depth(symbol, 50)

        asks = []
        for unit in depth['data']['asks']:
            price = float(unit['price'])
            amount = float(unit['amount'])
            asks.insert(0, OrderbookItem(price, amount))

        bids = []
        for unit in depth['data']['bids']:
            price = float(unit['price'])
            amount = float(unit['amount'])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
