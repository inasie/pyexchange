import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.okex.okex import OKEx


class ExchangeOKEx(ExchangeBase):
    """
    OKEx
    """
    NAME = 'OKEx'
    VERSION = 'v1'
    URL = 'https://github.com/okcoin-okex/API-docs-OKEx.com'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.okex = OKEx()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        pairs = self.okex.get_pairs()
        currency_pairs = []
        for pair_line in pairs.split('\n')[1:]:
            pair = pair_line.split(',')[1]
            base_currency = pair.split('_')[1].upper()
            currency = pair.split('_')[0].upper()
            currency_pairs.append(CurrencyPair(base_currency, currency))
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
        symbol = currency_pair.currency.lower() + '_' + currency_pair.base_currency.lower()
        logging.info('symbol: ' + symbol)
        ticker = self.okex.get_ticker(symbol)
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
        symbol = currency_pair.currency.lower() + '_' + currency_pair.base_currency.lower()
        orderbook = self.okex.get_depth(symbol)

        # timestamp = orderbook['data']['timestamp']
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
