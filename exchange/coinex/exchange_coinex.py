import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.coinex.coinex import CoinEx


class ExchangeCoinEx(ExchangeBase):
    """
    CoinEx
    """
    NAME = 'CoinEx'
    VERSION = 'v1'
    URL = 'https://github.com/coinexcom/coinex_exchange_api/wiki'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._ex = CoinEx()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        market_list = self._ex.get_market_list()

        markets = ['BCH', 'BTC', 'ETH', 'USDT']

        for market in market_list['data']:
            for m in markets:
                if market.endswith(m):
                    market_currency = m
                    currency = market[0:len(market)-len(m)]
                    currency_pairs.append(
                        CurrencyPair(market_currency, currency))
                    break
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
        market = currency_pair.currency + currency_pair.market_currency
        ticker = self._ex.get_ticker(market)
        timestamp = int(ticker['data']['date'])
        price = float(ticker['data']['ticker']['last'])
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
        market = currency_pair.currency + currency_pair.market_currency
        depth = self._ex.get_depth(market, '0', limit=20)

        asks = []
        for unit in depth['data']['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in depth['data']['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
