# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class CoinbasePro:
    """
    Coinbase Pro
    https://docs.pro.coinbase.com/
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_products(self):
        '''
        Get Products
        Get a list of available currency pairs for trading.
        https://docs.pro.coinbase.com/#get-products
        :return: json array
        '''
        URL = 'https://api.pro.coinbase.com/products'
        return self._http.get(URL)

    def get_product_order_book(self, id, level=None):
        '''
        Get Product Order Book
        Get a list of open orders for a product. The amount of detail shown can be customized with the level parameter.
        https://docs.pro.coinbase.com/#get-product-order-book
        :param str id: product id
        :param int level: default(1), Select response detail. Valid levels are documented below
            1	Only the best bid and ask
            2	Top 50 bids and asks (aggregated)
            3	Full order book (non aggregated)
        :return: json object
        '''
        URL = 'https://api.pro.coinbase.com/products/%s/book' % id
        params = {}
        if level is not None:
            params['level'] = level
        return self._http.get(URL, params)

    def get_product_ticker(self, id):
        '''
        Get Product Ticker
        Snapshot information about the last trade (tick), best bid/ask and 24h volume.
        https://docs.pro.coinbase.com/#get-product-ticker
        :param str id: product id
        :return: json object
        '''
        URL = 'https://api.pro.coinbase.com/products/%s/ticker' % id
        return self._http.get(URL)

    def get_trades(self, id):
        '''
        Get Product Trades
        List the latest trades for a product.
        https://docs.pro.coinbase.com/#get-trades
        :param str id: product id
        :return: json array
        '''
        URL = 'https://api.pro.coinbase.com/products/%s/trades' % id
        return self._http.get(URL)

    def get_historical_rates(self, id, start=None, end=None, granularity=None):
        '''
        Get Historic Rates
        Historic rates for a product. Rates are returned in grouped buckets based on requested granularity.
        https://docs.pro.coinbase.com/#get-historic-rates
        :param str id: product id
        :param str start: Start time in ISO 8601
        :param str end: End time in ISO 8601
        :param int granularity: Desired timeslice in seconds
            The granularity field must be one of the following values:
            {60, 300, 900, 3600, 21600, 86400}.
            Otherwise, your request will be rejected.
            These values correspond to timeslices representing one minute,
            five minutes, fifteen minutes, one hour, six hours, and one day, respectively.
        '''
        URL = 'https://api.pro.coinbase.com/products/%s/candles' % id
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if granularity is not None:
            params['granularity'] = granularity
        return self._http.get(URL, params)

    def get_24hr_stats(self, id):
        '''
        Get 24hr Stats
        Get 24 hr stats for the product. volume is in base currency units. open, high, low are in quote currency units.
        https://docs.pro.coinbase.com/#get-24hr-stats
        :param str id: product id
        :return: json object
        '''
        URL = 'https://api.pro.coinbase.com/products/%s/stats' % id
        return self._http.get(URL)

    def get_currencies(self):
        '''
        Get currencies
        List known currencies.
        https://docs.pro.coinbase.com/#get-currencies
        :return: json array
        '''
        URL = 'https://api.pro.coinbase.com/currencies'
        return self._http.get(URL)

    def get_time(self):
        '''
        Get the API server time.
        https://docs.pro.coinbase.com/#time
        :return: json object
        '''
        URL = 'https://api.pro.coinbase.com/time'
        return self._http.get(URL)
