# -*- coding: utf-8 -*-
import logging
from urllib3.request import urlencode
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Gopax():
    """
    Gopax
    https://www.gopax.co.kr/API
    """

    def __init__(self):
        self._http = HttpUtil()

    def get_asset(self):
        '''
        1. 자산 조회하기
        https://www.gopax.co.kr/API
        :return: json array
        '''
        URL = 'https://api.gopax.co.kr/assets'
        return self._http.get(URL)

    def get_trading_pairs(self):
        '''
        2. 특정 거래쌍 조회하기
        https://www.gopax.co.kr/API
        :return: json array
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs'
        return self._http.get(URL)

    def get_ticker(self, pair):
        '''
        3. 특정 거래쌍의 거래량 조회하기
        https://www.gopax.co.kr/API
        :param str pair: currency pair
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/%s/ticker' % pair
        return self._http.get(URL)

    def get_book(self, pair, level):
        '''
        4. 특정 거래쌍의 호가창 조회하기
        https://www.gopax.co.kr/API
        :param str pair: currency pair
        :parm int level: 호가창의 상세정보 수준 (1 = 매수호가 및 매도호가, 2 = 매수 및 매도 주문 각 50개, 기타 = 호가창 전체)
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/%s/book' % pair
        params = {'level': level}
        return self._http.get(URL, params)

    def get_trades(self, pair, limit=None, pastmax=None, latestmin=None, after=None, before=None):
        '''
        5. 최근 체결 내역 조회하기
        https://www.gopax.co.kr/API
        :param str pair: currency pair
        :parm int limit: 반환되는 항목의 갯수 (최대 100)
        :parm int pastmax: 이 ID보다 오래된 데이터를 제외함
        :parm int latestmin: 이 ID보다 새로운 최신 데이터를 가져옴
        :parm int after: 이 타임스탬프 이후의 데이터를 제외함 (ms 단위)
        :parm int before: 이 타임스탬프 이전의 데이터를 제외함 (ms 단위)
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/%s/trades' % pair
        params = {}
        if limit is not None:
            params['limit'] = limit
        if pastmax is not None:
            params['pastmax'] = pastmax
        if latestmin is not None:
            params['latestmin'] = latestmin
        if after is not None:
            params['after'] = after
        if before is not None:
            params['before'] = before
        return self._http.get(URL, params)

    def get_stats(self, pair):
        '''
        6. 특정 거래쌍의 최근 24시간 통계 조회하기
        https://www.gopax.co.kr/API
        :param str pair: currency pair
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/%s/stats' % pair
        return self._http.get(URL)

    def get_candles(self, pair, interval, start=None, end=None):
        '''
        7. 특정 거래쌍의 과거 기록 조회하기
        # 동작 안됨
        https://www.gopax.co.kr/API
        :param str pair: currency pair
        :param int interval: 희망하는 시간 간격 (분 단위, 1/5/30/1440)
        :param int start: 시작 시점 (ms단위)
        :param int end: 종료 시점 (ms단위)
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/%s/candles' % pair
        params = {}
        if start is not None:
            params['start'] = start
        if end is not None:
            params['end'] = end
        if interval is not None:
            params['interval'] = interval
        return self._http.get(URL, params)

    def get_all_stats(self):
        '''
        8. 모든 거래쌍의 최근 24시간 통계 조회하기
        https://www.gopax.co.kr/API
        :return: json object
        '''
        URL = 'https://api.gopax.co.kr/trading-pairs/stats'
        return self._http.get(URL)
