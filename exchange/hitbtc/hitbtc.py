# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class HitBTC():
    """
    HitBTC
    https://api.hitbtc.com/
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_currencies(self):
        '''
        Return the actual list of available currencies, tokens, ICO etc.
        https://api.hitbtc.com/#currencies
        :return: json array
        '''
        URL = 'https://api.hitbtc.com/api/2/public/currency'
        return self._http.get(URL)

    def get_symbols(self):
        '''
        Return the actual list of currency symbols (currency pairs) traded on HitBTC exchange.
        The first listed currency of a symbol is called the base currency,
        and the second currency is called the quote currency.
        The currency pair indicates how much of the quote currency is needed to purchase one unit of the base currency.
        https://api.hitbtc.com/#symbols
        :return: json array
        '''
        URL = 'https://api.hitbtc.com/api/2/public/symbol'
        return self._http.get(URL)

    def get_tickers(self):
        '''
        Return ticker information
        https://api.hitbtc.com/#tickers
        :return: json array
        '''
        URL = 'https://api.hitbtc.com/api/2/public/ticker'
        return self._http.get(URL)

    def get_ticker(self, symbol):
        '''
        Return ticker information
        https://api.hitbtc.com/#tickers
        :param str symbol:
        :return: json object
        '''
        URL = 'https://api.hitbtc.com/api/2/public/ticker/%s' % symbol
        return self._http.get(URL)

    def get_trades(self, symbol, sort=None, by=None, _from=None, till=None, limit=None, offset=None):
        '''
        Return trade data
        https://api.hitbtc.com/#trades
        :param str symbol:
        :param str sort: Default DESC
        :param str by: Filtration definition. Accepted values: id, timestamp. Default timestamp
        :param int _from:
        :param int till:
        :param int limit:
        :param int offset:
        :return: json array
        '''
        URL = 'https://api.hitbtc.com/api/2/public/trades/%s' % symbol
        params = {}
        if sort is not None:
            params['sort'] = sort
        if by is not None:
            params['by'] = by
        if _from is not None:
            params['from'] = _from
        if till is not None:
            params['till'] = till
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        return self._http.get(URL, params)

    def get_orderbook(self, symbol, limit=None):
        '''
        An order book is an electronic list of buy and sell orders for a specific symbol, organized by price level.
        https://api.hitbtc.com/#orderbook
        :param str symbol:
        :param itn limit: Limit of orderbook levels, default 100. Set 0 to view full orderbook levels
        :return: json object
        '''
        URL = 'https://api.hitbtc.com/api/2/public/orderbook/%s' % symbol
        params = {}
        if limit is not None:
            params['limit'] = limit
        return self._http.get(URL, params)

    def get_candles(self, symbol, limit=None, period=None):
        '''
        An candles used for OHLC a specific symbol.
        https://api.hitbtc.com/#candles
        :param str symbol:
        :param int limit: Limit of candles, default 100.
        :param string period: One of: M1 (one minute), M3, M5, M15, M30, H1, H4, D1, D7, 1M (one month). Default is M30 (30 minutes).
        :return: json array
        '''
        URL = 'https://api.hitbtc.com/api/2/public/candles/%s' % symbol
        params = {}
        if limit is not None:
            params['limit'] = limit
        if period is not None:
            params['period'] = period
        return self._http.get(URL, params)
