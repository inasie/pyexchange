from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.upbit.upbit import Upbit


class ExchangeUpbit(ExchangeBase):
    """
    Upbit
    """
    NAME = 'Upbit'
    VERSION = 'v1.0'
    URL = 'https://docs.upbit.com/v1.0/reference'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.upbit = Upbit()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        market_all = self.upbit.get_market_all()
        for market in market_all:
            tmp = market['market'].split('-')
            currency_pairs.append(CurrencyPair(tmp[0], tmp[1]))
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
        base_currency = currency_pair.base_currency
        currency = currency_pair.currency
        ticker = self.upbit.get_ticker(['%s-%s' % (base_currency, currency)])

        price = ticker[0]['trade_price']
        timestamp = ticker[0]['timestamp']
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
        base_currency = currency_pair.base_currency
        currency = currency_pair.currency
        market = '%s-%s' % (base_currency, currency)
        orderbook = self.upbit.get_orderbook([market])

        timestamp = orderbook[0]['timestamp']
        asks = []
        bids = []
        for unit in orderbook[0]['orderbook_units']:
            asks.append(OrderbookItem(unit['ask_price'], unit['ask_size']))
            bids.append(OrderbookItem(unit['bid_price'], unit['bid_size']))

        return Orderbook(currency_pair, asks, bids, timestamp)
