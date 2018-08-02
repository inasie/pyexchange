# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class CoinEx:
    """
    CoinEx
    https://github.com/coinexcom/coinex_exchange_api/wiki
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_market_list(self):
        '''
        Acquire Market List
        https://github.com/coinexcom/coinex_exchange_api/wiki/020market
        :return: json object
        '''
        URL = 'https://api.coinex.com/v1/market/list'
        return self._http.get(URL)

    def get_ticker(self, market):
        '''
        Acquire Market Statistics
        https://github.com/coinexcom/coinex_exchange_api/wiki/021ticker#acquire-market-statistics
        :param str market:
        :return: json object
        '''
        URL = 'https://api.coinex.com/v1/market/ticker'
        params = {'market': market}
        return self._http.get(URL, params)

    def get_depth(self, market, merge, limit=None):
        '''
        Acquire Market Depth
        https://github.com/coinexcom/coinex_exchange_api/wiki/022depth#acquire-market-depth
        :param str market:
        :param str merge: '0', '0.1', '0.01', '0.001', '0.0001', '0.00001', '0.000001', '0.0000001', '0.00000001
        :param int limit: Return amount，range: 5/10/20
        :return: json object
        '''
        URL = 'https://api.coinex.com/v1/market/depth'
        params = {
            'market': market,
            'merge': merge
        }
        if limit is not None:
            params['limit'] = limit
        return self._http.get(URL, params)

    def get_deals(self, market, last_id=None):
        '''
        Acquire Latest Transaction Data
        https://github.com/coinexcom/coinex_exchange_api/wiki/023deals#acquire-latest-transaction-data
        :param str market:
        :param int last_id: Transaction history id, send 0 to draw from the latest record.
        :return: json object
        '''
        URL = 'https://api.coinex.com/v1/market/deals'
        params = {
            'market': market
        }
        if last_id is not None:
            params['last_id'] = last_id
        return self._http.get(URL, params)

    def get_kline(self, market, type, limit=None):
        '''
        Acquire K-Line Data
        https://github.com/coinexcom/coinex_exchange_api/wiki/024kline#acquire-k-line-data
        :param str market:
        :param str type:
            1min:1min;
            3min:3min;
            5min:5min;
            15min:15min;
            30min:30min;
            1hour:1hour;
            2hour:2hour;
            4hour:4hour;
            6hour:6hour;
            12hour:12hour;
            1day:1day;
            3day:3day;
            1week:1week;
        :param int limit: Less than or equal to 1000
        '''
        URL = 'https://api.coinex.com/v1/market/kline'
        params = {
            'market': market,
            'type': type
        }
        if limit is not None:
            params['limit'] = limit
        return self._http.get(URL, params)
