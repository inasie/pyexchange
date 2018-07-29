import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.gopax.gopax import Gopax


class ExchangeGopax(ExchangeBase):
    """
    Gopax
    """
    NAME = 'Gopax'
    VERSION = 'Unknown'
    URL = 'https://www.gopax.co.kr/API'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._gopax = Gopax()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        trading_pairs = self._gopax.get_trading_pairs()

        for pair_obj in trading_pairs:
            base = pair_obj['baseAsset']
            quote = pair_obj['quoteAsset']
            currency_pairs.append(CurrencyPair(quote, base))

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

        currency = currency_pair.currency + '-' + currency_pair.market_currency
        ticker = self._gopax.get_ticker(currency)
        price = float(ticker['price'])
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
        currency = currency_pair.currency + '-' + currency_pair.market_currency
        orderbook = self._gopax.get_book(currency, 2)

        asks = []
        for unit in orderbook['ask']:
            price = float(unit[1])
            amount = float(unit[2])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['bid']:
            price = float(unit[1])
            amount = float(unit[2])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
