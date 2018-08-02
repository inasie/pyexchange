import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.lbank.lbank import LBank


class ExchangeLBank(ExchangeBase):
    """
    LBank
    """
    NAME = 'LBank'
    VERSION = 'v1'
    URL = 'https://github.com/LBank-exchange/lbank-official-api-docs'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._lb = LBank()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        pairs = self._lb.get_currency_pairs()

        for pair in pairs:
            market_currency = pair.split('_')[1].upper()
            currency = pair.split('_')[0].upper()
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
        symbol = currency_pair.currency.lower() + '_' + currency_pair.market_currency.lower()
        ticker = self._lb.get_ticker(symbol)
        timestamp = ticker['timestamp']
        price = float(ticker['ticker']['latest'])
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
        symbol = currency_pair.currency.lower() + '_' + currency_pair.market_currency.lower()
        depth = self._lb.get_depth(symbol, 50)

        asks = []
        for unit in depth['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in depth['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
