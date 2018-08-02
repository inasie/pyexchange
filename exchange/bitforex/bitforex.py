# -*- coding: utf-8 -*-
import logging
import time
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Bitforex():
    """
    Bitforex
    https://github.com/bitforexapi/API_Doc_en/wiki
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_symbols(self):
        '''
        Symbol Information
        https://github.com/bitforexapi/API_Doc_en/wiki/Symbol-Information
        :return: json object
        '''
        URL = 'https://api.bitforex.com/api/v1/market/symbols'
        return self._http.get(URL)

    def get_ticker(self, symbol):
        '''
        Ticker Information
        https://github.com/bitforexapi/API_Doc_en/wiki/Ticker-Information
        :param str symbol: Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
        :return: json object
        '''
        URL = 'https://api.bitforex.com/api/v1/market/ticker'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_depth(self, symbol, size=None):
        '''
        Depth information
        https://github.com/bitforexapi/API_Doc_en/wiki/Depth-information
        :param str symbol: Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
        :param int size: Orders Depth Quantity 1-200, default(5)
        :return: json object
        '''
        URL = 'https://api.bitforex.com/api/v1/market/depth'
        params = {'symbol': symbol}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_trades(self, symbol, size=None):
        '''
        Trading record information
        https://github.com/bitforexapi/API_Doc_en/wiki/Trading-record-information
        :param str symbol: Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
        :param int size: The number of transactions is 1-600, default(1)
        :return: json object
        '''
        URL = 'https://api.bitforex.com/api/v1/market/trades'
        params = {'symbol': symbol}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_kline(self, symbol, ktype, size=None):
        '''
        K Line information
        https://github.com/bitforexapi/API_Doc_en/wiki/K-Line-information
        :param str symbol: Trading pairs such as coin-usd-btc, coin-usd-eth, etc.
        :param str ktype: K line type:
            1min: one minute K line
            5min: five minutes K line
            15min: 15 minutes K line
            30min: thirty minutes K line
            1hour: one hour K Line
            2hour: Two hours K line
            4hour: Four hours K line
            12hour: 12 hours K line
            1day: Daily K line
            1 week: Weekly K line
            1month: monthly K line
        :param int size: Number of K lines 1-600, default(1)
        :return: json object
        '''
        URL = 'https://api.bitforex.com/api/v1/market/kline'
        params = {'symbol': symbol, 'ktype': ktype}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)
