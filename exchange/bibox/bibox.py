# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class Bibox:
    """
    Bibox
    https://github.com/Biboxcom/api_reference/wiki/home_en
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_pair_list(self):
        '''
        get pair list
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {'cmd': 'pairList'}
        return self._http.get(URL, params)

    def get_kline(self, pair, period, size=None):
        '''
        get K line
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :param str pair: pairs, exmple: BIX_BTC
        :param str period: k line period，value ['1min', '3min', '5min', '15min', '30min', '1hour', '2hour', '4hour', '6hour', '12hour', 'day', 'week']
        :param int size: how many，1-1000，if not passed will return 1000
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'kline',
            'pair': pair,
            'period': period
        }
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_depth(self, pair, size=None):
        '''
        get depth
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :param str pair: pairs，example: BIX_BTC
        :param int size: how many，1-200，if not passed will return 200
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'depth',
            'pair': pair
        }
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_trade_history(self, pair, size=None):
        '''
        get trade history
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :param str pair: pairs，example: BIX_BTC
        :param int size: how many，1-200，if not passed will return 200
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'deals',
            'pair': pair
        }
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_ticker(self, pair):
        '''
        get ticker
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :param str pair: pairs，example: BIX_BTC
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'ticker',
            'pair': pair
        }
        return self._http.get(URL, params)

    def get_market_all(self):
        '''
        get market data (all pairs)
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'marketAll'
        }
        return self._http.get(URL, params)

    def get_market(self, pair):
        '''
        get market
        https://github.com/Biboxcom/api_reference/wiki/home_en#323-v1mdata
        :param str pair: pairs，example: BIX_BTC
        :return: json object
        '''
        URL = 'https://api.bibox.com/v1/mdata'
        params = {
            'cmd': 'market',
            'pair': pair
        }
        return self._http.get(URL, params)
