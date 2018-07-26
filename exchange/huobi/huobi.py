# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Huobi():
    """
    Huobi Pro
    https://github.com/huobiapi/API_Docs_en/wiki
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_history_kline(self, symbol, period, size=None):
        '''
        Get Candlestick Data
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-markethistorykline--get-candlestick-data
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...
        :param str period: 1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year
        :param integer size: default(150), [1,2000]
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/history/kline'
        params = {
            'symbol': symbol,
            'period': period
        }
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_market_detail_merged(self, symbol):
        '''
        Get Ticker
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-marketdetailmerged-get-ticker
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/detail/merged'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_market_tickers(self):
        '''
        Get Tickers
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-markettickers
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/tickers'
        return self._http.get(URL)

    def get_market_depth(self, symbol, type):
        '''
        Market Depth
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-marketdepth---market-depth
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...
        :param str type: Depth data type, step0, step1, step2, step3, step4, step5
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/depth'
        params = {
            'symbol': symbol,
            'type': type
        }
        return self._http.get(URL, params)

    def get_market_trade(self, symbol):
        '''
        Trade Detail
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-markettrade--trade-detail
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/trade'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_market_history_trade(self, symbol, size=None):
        '''
        Orderbook
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-markethistorytrade-orderbook
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...:param:
        :param int size: default(1), [1, 2000]
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/history/trade'
        params = {'symbol': symbol}
        if size is not None:
            params['size'] = size
        return self._http.get(URL, params)

    def get_market_detail(self, symbol):
        '''
        Market detail in 24 hours
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-marketdetail---market-detail-in-24-hours
        :param str symbol: trading asset, btcusdt, bccbtc, rcneth ...:param:
        :return: json object
        '''
        URL = 'https://api.huobi.pro/market/detail'
        params = {'symbol': symbol}
        return self._http.get(URL, params)

    def get_symbols(self):
        '''
        Get all the trading assets in huobi.pro
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-v1commonsymbols-----get-all-the-trading-assets-in-huobipro
        :return: json object
        '''
        URL = 'https://api.huobi.pro/v1/common/symbols'
        return self._http.get(URL)

    def get_currencys(self):
        '''
        Get currencys supported in huobi.pro
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-v1commoncurrencys-----get-currencys-supported-in-huobipro
        :return: json object
        '''
        URL = 'https://api.huobi.pro/v1/common/currencys'
        return self._http.get(URL)

    def get_timestamp(self):
        '''
        Get system timestamp
        https://github.com/huobiapi/API_Docs_en/wiki/REST_Reference#get-v1commontimestamp----get-system-timestamp
        :return: json object
        '''
        URL = 'https://api.huobi.pro/v1/common/timestamp'
        return self._http.get(URL)
