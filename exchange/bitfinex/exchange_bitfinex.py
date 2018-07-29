from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bitfinex.bitfinex import Bitfinex


class ExchangeBitfinex(ExchangeBase):
    """
    Bitfinex
    """
    NAME = 'Bitfinex'
    VERSION = 'v1'
    URL = 'https://bitfinex.readme.io/v1/reference'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.bitfinex = Bitfinex()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        symbols = self.bitfinex.get_symbols()
        for symbol in symbols:
            currency = symbol[0:3].upper()
            market_currency = symbol[3:].upper()
            currency_pairs.append(CurrencyPair(market_currency, currency))
        return currency_pairs

    def get_ticker(self, currency_pair):
        '''
        Gets last price
        :param CurrencyPair currency_pair: currency pair
        :return: ticker
        :rtype: Ticker
        '''
        symbol = currency_pair.currency + currency_pair.market_currency
        ticker = self.bitfinex.get_ticker(symbol)
        timestamp = int(float(ticker['timestamp']))
        price = float(ticker['last_price'])
        return Ticker(currency_pair, price, timestamp)

    def get_orderbook(self, currency_pair):
        '''
        Gets orderbook information
        :param CurrencyPair currency_pair: currency pair
        :return: orderbook
        :rtype: Orderbook
        '''
        symbol = currency_pair.currency + currency_pair.market_currency
        orderbook = self.bitfinex.get_orderbook(symbol)

        timestamp = 0
        bids = []
        for unit in orderbook['bids']:
            price = float(unit['price'])
            amount = float(unit['amount'])
            timestamp = int(float(unit['timestamp']))
            bids.append(OrderbookItem(price, amount))
        asks = []
        for unit in orderbook['asks']:
            price = float(unit['price'])
            amount = float(unit['amount'])
            timestamp = int(float(unit['timestamp']))
            asks.append(OrderbookItem(price, amount))
        return Orderbook(currency_pair, asks, bids, timestamp)
