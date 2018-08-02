# -*- coding: utf-8 -*-
import logging
import time
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class LBank():
    """
    LBank
    https://github.com/LBank-exchange/lbank-official-api-docs
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_ticker_all(self):
        '''
        Get all ticker
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :return: json array
        '''
        URL = 'http://api.lbank.info/v1/ticker.do'
        params = {'symbol': 'all'}
        return self._http.get(URL, params)

    def get_ticker(self, symbol):
        '''
        Get all ticker
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :param str symbol:
        :return: json object
        '''
        URL = 'http://api.lbank.info/v1/ticker.do'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_currency_pairs(self):
        '''
        Get currency pairs
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :return: json array
        '''
        URL = 'http://api.lbank.info/v1/currencyPairs.do'
        return self._http.get(URL)

    def get_depth(self, symbol, size, merge=None):
        '''
        Get depth
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :param str symbol: symbol
        :param int size: 1-60 (default 60)
        :param int merge: 0, 1 (default 0)
        :return: json array
        '''
        URL = 'http://api.lbank.info/v1/depth.do'
        params = {'symbol': symbol, 'size': size}
        if merge is not None:
            params['merge'] = merge
        return self._http.get(URL, params)

    def get_trades(self, symbol, size, time=None):
        '''
        Get trades
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :param str symbol: symbol
        :param int size: 1-600 (default 600)
        :param str time:
        :return: json array
        '''
        URL = 'http://api.lbank.info/v1/trades.do'
        params = {'symbol': symbol, 'size': size}
        return self._http.get(URL, params)

    def get_kline(self, symbol, size, type, time=None):
        '''
        Get kline
        https://github.com/LBank-exchange/lbank-official-api-docs/blob/master/API-For-Spot-CN/%E5%B8%81%E5%B8%81%E4%BA%A4%E6%98%93REST%20API(%E8%A1%8C%E6%83%85).md#%E5%B8%81%E5%B8%81%E8%A1%8C%E6%83%85-api
        :param str symbol: symbol
        :param int size: 1-2880
        :param str type:
            minute1：1分钟
            minute5：5分钟
            minute15：15分钟
            minute30：30分钟
            hour1：1小时
            hour4：4小时
            hour8：8小时
            hour12：12小时
            day1：1日
            week1：1周
        :param string time:
        :return: json array
        '''
        URL = 'http://api.lbank.info/v1/kline.do'
        params = {
            'symbol': symbol,
            'size': size,
            'type': type,
            'time': time
        }
        return self._http.get(URL, params)
