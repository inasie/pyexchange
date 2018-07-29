# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class OKEx():
    """
    OKEx Spot
    https://github.com/okcoin-okex/API-docs-OKEx.com
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_pairs(self):
        URL = 'https://raw.githubusercontent.com/okcoin-okex/API-docs-OKEx.com/master/%E5%B8%81%E5%AF%B9%E7%B2%BE%E5%BA%A6(pairs_increment).csv'
        return self._http.get_raw(URL)

    def get_ticker(self, symbol, contract_type=None):
        '''
        Get Price Ticker
        https://github.com/okcoin-okex/API-docs-OKEx.com/blob/master/API-For-Spot-EN/REST%20API%20for%20SPOT.md#spot-price-api
        :param str symbol: Pairs like : ltc_btc etc_btc
        :param str contract_type: this_week next_week quarter
        :return: json object
        '''
        URL = 'https://www.okex.com/api/v1/ticker.do'
        params = {
            'symbol': symbol
        }
        if contract_type is not None:
            params['contract_type'] = contract_type
        return self._http.get(URL, params=params)

    def get_depth(self, symbol, size=None):
        '''
        Get Market Depth
        https://github.com/okcoin-okex/API-docs-OKEx.com/blob/master/API-For-Spot-EN/REST%20API%20for%20SPOT.md#spot-price-api
        :param str symbol: Pairs like : ltc_btc etc_btc
        :param int size: value: must be between 1 - 200
        :return: json object
        '''
        URL = 'https://www.okex.com/api/v1/depth.do'
        params = {
            'symbol': symbol
        }
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params=params)

    def get_trades(self, symbol, since=None):
        '''
        Get Trade Recently 600
        https://github.com/okcoin-okex/API-docs-OKEx.com/blob/master/API-For-Spot-EN/REST%20API%20for%20SPOT.md#spot-price-api
        :param str symbol: Pairs like : ltc_btc etc_btc
        :param int since: value: get recently 600 pieces of data starting from the given tid (optional)
        :return: json array
        '''
        URL = 'https://www.okex.com/api/v1/trades.do'
        params = {'symbol': symbol}
        if since is not None:
            params['since'] = since
        return self._http.get(URL, params=params)

    def get_kline(self, symbol, type, size=None, since=None):
        '''
        Get Candlestick Data
        https://github.com/okcoin-okex/API-docs-OKEx.com/blob/master/API-For-Spot-EN/REST%20API%20for%20SPOT.md#spot-price-api
        :param str symbol: Pairs like : ltc_btc etc_btc
        :param str type: 1min/3min/5min/15min/30min/1day/3day/1week/1hour/2hour/4hour/6hour/12hour
        :param int size: specify data size to be acquired
        :param int since: timestamp(eg:1417536000000). data after the timestamp will be returned
        '''
        URL = 'https://www.okex.com/api/v1/kline.do'
        params = {
            'symbol': symbol,
            'type': type
        }
        if size is not None:
            params['size'] = size
        if since is not None:
            params['since'] = since
        return self._http.get(URL, params=params)
