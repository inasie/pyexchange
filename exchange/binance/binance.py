# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class Binance:
    """
    Binance
    https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md
    """

    def __init__(self):
        self.http = HttpUtil()

    def get_ping(self):
        '''
        Test connectivity
        Test connectivity to the Rest API.
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#test-connectivity
        :return: json object
        '''
        URL = 'https://api.binance.com/api/v1/ping'
        return self.http.get(URL)

    def get_time(self):
        '''
        Check server time
        Test connectivity to the Rest API and get the current server time.
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#check-server-time
        :return: json object
        '''
        URL = 'https://api.binance.com/api/v1/time'
        return self.http.get(URL)

    def get_exchange_info(self):
        '''
        Exchange information
        Current exchange trading rules and symbol information
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#exchange-information
        :return: json object
        '''
        URL = 'https://api.binance.com/api/v1/exchangeInfo'
        return self.http.get(URL)

    def get_orderbook(self, symbol, limit=None):
        '''
        Order book
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#order-book
        Caution: setting limit=0 can return a lot of data.
        :param str symbol:
        :param int limit: Default 100; max 1000. Valid limits:[5, 10, 20, 50, 100, 500, 1000]
        :return: json object
        '''
        URL = 'https://api.binance.com/api/v1/depth'
        if limit is not None and limit not in [5, 10, 20, 50, 100, 500, 1000]:
            raise InvalidParamException('invalid unit: %d' % limit)

        params = {'symbol': symbol}
        if limit is not None:
            params['limit'] = limit
        return self.http.get(URL, params=params)

    def get_trades(self, symbol, limit=None):
        '''
        Recent trades list
        Get recent trades (up to last 500).
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#recent-trades-list
        :param str symbol:
        :param int limit: Default 500; max 1000
        :return: json array
        '''
        URL = 'https://api.binance.com/api/v1/trades'
        params = {'symbol': symbol}
        if limit is not None:
            params['limit'] = limit
        return self.http.get(URL, params=params)

    def get_agg_trades(self, symbol, from_id=None, start_time=None, end_time=None, limit=None):
        '''
        Compressed/Aggregate trades list
        Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated.
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#compressedaggregate-trades-list
        :param str symbol:
        :param long from_id: ID to get aggregate trades from INCLUSIVE.
        :param long start_time: Timestamp in ms to get aggregate trades from INCLUSIVE.
        :param long end_time: Timestamp in ms to get aggregate trades until INCLUSIVE.
        :param int limit: Default 500; max 1000.
        :return: json array
        '''
        URL = 'https://api.binance.com/api/v1/aggTrades'
        params = {'symbol': symbol}
        if from_id is not None:
            params['fromId'] = from_id
        if start_time is not None:
            params['startTime'] = start_time
        if end_time is not None:
            params['endTime'] = end_time
        if limit is not None:
            params['limit'] = limit
        return self.http.get(URL, params=params)

    def get_klines(self, symbol, interval, start_time=None, end_time=None, limit=None):
        '''
        Kline/Candlestick data
        Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#klinecandlestick-data
        :param str symbol:
        :param str interval: https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#enum-definitions
        :param long start_time: Timestamp in ms to get aggregate trades from INCLUSIVE.
        :param long end_time: Timestamp in ms to get aggregate trades until INCLUSIVE.
        :param int limit: Default 500; max 1000.
        :return: json array
        '''
        URL = 'https://api.binance.com/api/v1/klines'

        if interval not in ['1m', '3m', '5m', '15m', '30m',
                            '1h', '2h', '4h', '6h', '8h', '12h',
                            '1d', '3d', '1w', '1M']:
            raise InvalidParamException('invalid interval: %s' % interval)

        params = {
            'symbol': symbol,
            'interval': interval
        }
        if start_time is not None:
            params['startTime'] = start_time
        if end_time is not None:
            params['endTime'] = end_time
        if limit is not None:
            params['limit'] = limit
        return self.http.get(URL, params=params)

    def get_24h_ticker(self, symbol=None):
        '''
        24hr ticker price change statistics
        24 hour price change statistics. Careful when accessing this with no symbol.
        https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md#24hr-ticker-price-change-statistics
        :param str symbol:
        :return: json array (symbol is None), json object (symbol is not None)
        '''
        URL = 'https://api.binance.com/api/v1/ticker/24hr'
        params = {}
        if symbol is not None:
            params['symbol'] = symbol
        return self.http.get(URL, params=params)

    def get_ticker_price(self, symbol=None):
        '''
        Symbol price ticker
        Latest price for a symbol or symbols.
        :param str symbol:
        :return: json array (symbol is None), json object (symbol is not None)
        '''
        URL = 'https://api.binance.com/api/v3/ticker/price'
        params = {}
        if symbol is not None:
            params['symbol'] = symbol
        return self.http.get(URL, params=params)

    def get_ticker_book(self, symbol=None):
        '''
        Symbol order book ticker
        Best price/qty on the order book for a symbol or symbols.
        :param str symbol:
        :return: json array (symbol is None), json object (symbol is not None)
        '''
        URL = 'https://api.binance.com/api/v3/ticker/bookTicker'
        params = {}
        if symbol is not None:
            params['symbol'] = symbol
        return self.http.get(URL, params=params)
