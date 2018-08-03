# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class Coinbene:
    """
    Coinbene
    https://github.com/Coinbene/API-Documents/wiki/0.0.0-Coinbene-API-documents
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_symbols(self):
        '''
        Get Symbols
        https://github.com/Coinbene/API-Documents/wiki/1.1.3-Get-Symbols-%5BMarket%5D
        :return: json object
        '''
        URL = 'http://api.coinbene.com/v1/market/symbol'
        return self._http.get(URL)

    def get_ticker_all(self):
        '''
        Get ticker (all)
        https://github.com/Coinbene/API-Documents/wiki/1.1.0-Get-Ticker-%5BMarket%5D
        :return: json object
        '''
        URL = 'http://api.coinbene.com/v1/market/ticker'
        params = {'symbol': 'all'}
        return self._http.get(URL, params)

    def get_ticker(self, symbol):
        '''
        Get ticker
        https://github.com/Coinbene/API-Documents/wiki/1.1.0-Get-Ticker-%5BMarket%5D
        :param str symbol: the code of symbol
        :return: json object
        '''
        URL = 'http://api.coinbene.com/v1/market/ticker'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_orderbook(self, symbol, depth=None):
        '''
        Get Orderbook
        https://github.com/Coinbene/API-Documents/wiki/1.1.1-Get-Orderbook-%5BMarket%5D
        :param str symbol: the code of symbol
        :param int depth: the number of orders, default = 200, 1 to 500
        :return: json object
        '''
        URL = 'http://api.coinbene.com/v1/market/orderbook'
        params = {'symbol': symbol}
        if depth is not None:
            params['depth'] = depth
        return self._http.get(URL, params)

    def get_trades(self, symbol, size=None):
        '''
        Get Trades
        https://github.com/Coinbene/API-Documents/wiki/1.1.2-Get-Trades-%5BMarket%5D
        :param str symbol: the code of symbol
        :param int size: The number of trade records, sorted by time reverse order. Default = 300, 1 to 2000
        :return: json object
        '''
        URL = 'http://api.coinbene.com/v1/market/trades'
        params = {'symbol': symbol}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)
