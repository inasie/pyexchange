# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Coinone():
    """
    Coinone
    https://doc.coinone.co.kr
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_ticker(self, currency):
        '''
        Ticker
        https://doc.coinone.co.kr/#api-Public-Ticker
        :param str currency: default(btc), btc, bch, eth, etc, xrp, qtum, iota, ltc, btg, omg, eos, data, zil, knc, zrx, all
        :return: json object
        '''
        URL = 'https://api.coinone.co.kr/ticker/'
        params = {'currency': currency}
        return self._http.get(URL, params)

    def get_ticker_utc(self, currency):
        '''
        Ticker UTC
        https://doc.coinone.co.kr/#api-Public-Ticker_UTC
        :param str currency: default(btc), btc, bch, eth, etc, xrp, qtum, iota, ltc, btg, omg, eos, data, zil, knc, zrx, all
        :return: json object
        '''
        URL = 'https://api.coinone.co.kr/ticker/'
        params = {'currency': currency}
        return self._http.get(URL, params)

    def get_orderbook(self, currency):
        '''
        Orderbook
        https://doc.coinone.co.kr/#api-Public-Orderbook
        :param str currency: default(btc), btc, bch, eth, etc, xrp, qtum, iota, ltc, btg, omg, eos, data, zil, knc, zrx
        :return: json object
        '''
        URL = 'https://api.coinone.co.kr/orderbook/'
        params = {'currency': currency}
        return self._http.get(URL, params)

    def get_trades(self, currency, period):
        '''
        Recent Complete Orders
        https://doc.coinone.co.kr/#api-Public-RecentTransactions
        :param str currency: default(btc), btc, bch, eth, etc, xrp, qtum, iota, ltc, btg, omg, eos, data, zil, knc, zrx
        :param str period: default(hour), hour/day
        :return: json object
        '''
        URL = 'https://api.coinone.co.kr/trades/'
        params = {
            'currency': currency,
            'period': period
        }
        return self._http.get(URL, params)
