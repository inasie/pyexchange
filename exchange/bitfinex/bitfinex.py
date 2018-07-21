# -*- coding: utf-8 -*-
import json
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Bitfinex():
    """
    Bitfinex
    https://bitfinex.readme.io/v1/reference
    """

    def __init__(self):
        self.http = HttpUtil()

    def get_ticker(self, symbol):
        '''
        Ticker
        The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day.
        https://bitfinex.readme.io/v1/reference#rest-public-ticker
        :param str symbol: The symbol you want information about. You can find the list of valid symbols by calling the /symbols endpoint.
        :return: json object
        '''
        URL = 'https://api.bitfinex.com/v1/ticker/'
        return self.http.get(URL + symbol)

    def get_stats(self, symbol):
        '''
        Stats
        Various statistics about the requested pair.
        https://bitfinex.readme.io/v1/reference#rest-public-stats
        :param str symbol: The symbol you want information about. You can find the list of valid symbols by calling the /symbols endpoint.
        :return: json array
        '''
        URL = 'https://api.bitfinex.com/v1/stats/'
        return self.http.get(URL + symbol)

    # https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
    def get_fundingbook(self, currency='USD', limit_bids=None, limit_asks=None):
        '''
        Fundingbook
        Get the full margin funding book
        https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
        :param str currency:
        :param int limit_bids: Default(50), Limit the number of funding bids returned. May be 0 in which case the array of bids is empty
        :param int limit_asks: Default(50), Limit the number of funding offers returned. May be 0 in which case the array of asks is empty
        :return: json object
        '''
        URL = 'https://api.bitfinex.com/v1/lendbook/'
        params = {}
        if limit_asks is not None:
            params['limit_asks'] = limit_asks
        if limit_bids is not None:
            params['limit_bids'] = limit_bids
        return self.http.get(URL + currency, params)

    # https://bitfinex.readme.io/v1/reference#rest-public-orderbook
    def get_orderbook(self, symbol, limit_bids=None, limit_asks=None, group=None):
        '''
        Orderbook
        Get the full order book.
        https://bitfinex.readme.io/v1/reference#rest-public-orderbook
        :param str symbol:
        :param int limit_bids: Default(50), Limit the number of bids returned. May be 0 in which case the array of bids is empty
        :param int limit_asks: Default(50), Limit the number of asks returned. May be 0 in which case the array of asks is empty
        :param int group: Default(1), If 1, orders are grouped by price in the orderbook. If 0, orders are not grouped and sorted individually
        :return: json object
        '''
        URL = 'https://api.bitfinex.com/v1/book/'
        params = {}
        if limit_bids is not None:
            params['limit_bids'] = limit_bids
        if limit_asks is not None:
            params['limit_asks'] = limit_asks
        if group is not None:
            params['group'] = group
        return self.http.get(URL + symbol, params)

    def get_trades(self, symbol, timestamp=None, limit_trades=None):
        '''
        Trades
        Get a list of the most recent trades for the given symbol.
        https://bitfinex.readme.io/v1/reference#rest-public-trades
        :param str symbol:
        :param time timestamp: Only show trades at or after this timestamp
        :param int limit_trades: Default(50), Limit the number of trades returned. Must be >= 1
        :return: json array
        '''
        URL = 'https://api.bitfinex.com/v1/trades/'
        params = {}
        if timestamp is not None:
            params['timestamp'] = timestamp
        if limit_trades is not None:
            params['limit_trades'] = limit_trades
        return self.http.get(URL + symbol, params)

    def get_lends(self, currency='USD', timestamp=None, limit_lends=None):
        '''
        Lends
        Get a list of the most recent funding data for the given currency: total amount provided and Flash Return Rate (in % by 365 days) over time.
        https://bitfinex.readme.io/v1/reference#rest-public-lends
        :param str currency:
        :param time timestamp: Only show data at or after this timestamp
        :param int limit_lends: Default(50), Limit the amount of funding data returned. Must be >= 1
        :return: json array
        '''
        URL = 'https://api.bitfinex.com/v1/lends/'
        params = {}
        if timestamp is not None:
            params['timestamp'] = timestamp
        if limit_lends is not None:
            params['limit_lends'] = limit_lends
        return self.http.get(URL + currency, params)

    def get_symbols(self):
        '''
        Symbols
        A list of symbol names.
        https://bitfinex.readme.io/v1/reference#rest-public-symbols
        :return: json array
        '''
        URL = 'https://api.bitfinex.com/v1/symbols'
        return self.http.get(URL)

    def get_symbol_details(self):
        '''
        Symbol Details
        Get a list of valid symbol IDs and the pair details.
        https://bitfinex.readme.io/v1/reference#rest-public-symbol-details
        :return: json array
        '''
        URL = 'https://api.bitfinex.com/v1/symbols_details'
        return self.http.get(URL)
