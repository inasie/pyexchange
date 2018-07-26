import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.huobi.huobi import Huobi


class ExchangeHuobi(ExchangeBase):
    """
    Huobi Pro
    """
    NAME = 'Huobi Pro'
    VERSION = 'v1'
    URL = 'https://github.com/huobiapi/API_Docs_en/wiki'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._huobi = Huobi()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        symbols = self._huobi.get_symbols()

        for symbol_obj in symbols['data']:
            base_currency = symbol_obj['quote-currency'].upper()
            currency = symbol_obj['base-currency'].upper()
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
        symbol = currency_pair.currency.lower() + currency_pair.base_currency.lower()
        detail_merged = self._huobi.get_market_detail_merged(symbol)
        timestamp = detail_merged['ts']
        price = detail_merged['tick']['close']
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
        symbol = currency_pair.currency.lower() + currency_pair.base_currency.lower()
        depth = self._huobi.get_market_depth(symbol, 'step0')

        timestamp = depth['ts']
        asks = []
        for unit in depth['tick']['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in depth['tick']['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids, timestamp)
