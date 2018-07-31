# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class ZB():
    """
    ZB
    https://www.zb.com/i/developer/restApi
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_markets(self):
        '''
        Get the enabled market information ( price, number of decimal places)
        https://www.zb.com/i/developer/restApi#config
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/markets'
        return self._http.get(URL)

    def get_all_ticker(self):
        '''
        All Ticker
        https://www.zb.com/i/developer/restApi#market
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/allTicker'
        return self._http.get(URL)

    def get_ticker(self, market):
        '''
        Price
        https://www.zb.com/i/developer/restApi#market
        :param str market: ex) btc_usdt
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/ticker'
        params = {'market': market}
        return self._http.get(URL, params)

    def get_depth(self, market, size=None):
        '''
        Market depth
        https://www.zb.com/i/developer/restApi#market
        :param str market: ex) btc_usdt
        :param int size: Positions are from 1-50, if there is a combination of depth, only return 5 positions depth
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/depth'
        params = {'market': market}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_trades(self, market, since=None):
        '''
        Get history trade data
        https://www.zb.com/i/developer/restApi#market
        :param str market: ex) btc_usdt
        :param int since: 50 items after designate transaction ID
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/trades'
        params = {'market': market}
        if since is not None:
            params['since'] = since
        return self._http.get(URL, params)

    def get_kline(self, market, type=None, since=None, size=None):
        '''
        K line
        https://www.zb.com/i/developer/restApi#market
        :param str market: ex) btc_usdt
        :param str type:
            1min
            3min
            5min
            15min
            30min
            1day
            3day
            1week
            1hour
            2hour
            4hour
            6hour
            12hour
        :param int since: From this timestamp
        :param int size: Limit of returning data(default 1000,it only return 1000 data if that more than 1000 date )
        :return: json object
        '''
        URL = 'http://api.zb.cn/data/v1/kline'
        params = {'market': market}
        if type is not None:
            params['type'] = type
        if since is not None:
            params['since'] = since
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)
