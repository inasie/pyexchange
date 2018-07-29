# -*- coding: utf-8 -*-
import json
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Bitflyer():
    """
    Bitflyer
    https://lightning.bitflyer.com/docs?lang=en
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_markets(self):
        '''
        Market List
        https://lightning.bitflyer.com/docs?lang=en#market-list
        :return: json array
        '''
        URL = 'https://api.bitflyer.com/v1/markets'
        return self._http.get(URL)

    def get_orderbook(self, product_code):
        '''
        Order Book
        https://lightning.bitflyer.com/docs?lang=en#order-book
        :param str product_code: Please specify a product_code or alias, as obtained from the Market List. If omitted, the value is set to "BTC_JPY". Only "BTC_USD" is available for U.S. accounts, and only "BTC_EUR" is available for European accounts.
        :return: json object
        '''
        URL = 'https://api.bitflyer.com/v1/board'
        params = {'product_code': product_code}
        return self._http.get(URL, params)

    def get_ticker(self, product_code):
        '''
        Ticker
        https://lightning.bitflyer.com/docs?lang=en#ticker
        :param str product_code: Please specify a product_code or alias, as obtained from the Market List. If omitted, the value is set to "BTC_JPY". Only "BTC_USD" is available for U.S. accounts, and only "BTC_EUR" is available for European accounts.
        :return: json object
        '''
        URL = 'https://api.bitflyer.com/v1/ticker'
        params = {'product_code': product_code}
        return self._http.get(URL, params)

    def get_executions(self, product_code, count=None, before=None, after=None):
        '''
        Execution History
        https://lightning.bitflyer.com/docs?lang=en#execution-history
        :param str product_code: Please specify a product_code or alias, as obtained from the Market List. If omitted, the value is set to "BTC_JPY". Only "BTC_USD" is available for U.S. accounts, and only "BTC_EUR" is available for European accounts.
        :param int count: Specifies the number of results. If this is omitted, the value will be 100.
        :param int before: Obtains data having an id lower than the value specified for this parameter.
        :param int after: Obtains data having an id higher than the value specified for this parameter.
        :return: json array
        '''
        URL = 'https://api.bitflyer.com/v1/executions'
        params = {'product_code': product_code}
        if count is not None:
            params['count'] = count
        if before is not None:
            params['before'] = before
        if after is not None:
            params['after'] = after
        return self._http.get(URL, params)

    def get_exchange_status(self, product_code, count=None, before=None, after=None):
        '''
        Exchange status
        https://lightning.bitflyer.com/docs?lang=en#exchange-status
        :param str product_code: Please specify a product_code or alias, as obtained from the Market List. If omitted, the value is set to "BTC_JPY". Only "BTC_USD" is available for U.S. accounts, and only "BTC_EUR" is available for European accounts.
        :return: json object
        '''
        URL = 'https://api.bitflyer.com/v1/gethealth'
        params = {'product_code': product_code}
        return self._http.get(URL, params)
