# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil
from urllib.parse import urlencode


class Upbit:
    """
    Upbit
    https://docs.upbit.com/v1.0/reference
    """

    def __init__(self):
        self.http = HttpUtil()

    def get_market_all(self):
        '''
        마켓 코드 조회
        업비트에서 거래 가능한 마켓 목록
        https://docs.upbit.com/v1.0/reference#%EB%A7%88%EC%BC%93-%EC%BD%94%EB%93%9C-%EC%A1%B0%ED%9A%8C
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/market/all'
        return self.http.get(URL)

    def get_minutes_candles(self, unit, market, to=None, count=None):
        '''
        분(Minute) 캔들
        https://docs.upbit.com/v1.0/reference#%EB%B6%84minute-%EC%BA%94%EB%93%A4-1
        :param int unit: 분 단위. 가능한 값 : 1, 3, 5, 15, 10, 30, 60, 240
        :param str market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param str to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX. 비워서 요청시 가장 최근 캔들
        :param int count: 캔들 개수
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/candles/minutes/%s' % str(unit)
        if unit not in [1, 3, 5, 10, 15, 30, 60, 240]:
            raise InvalidParamException('invalid unit: %s' % str(unit))

        params = {'market': market}
        if to is not None:
            params['to'] = to
        if count is not None:
            params['count'] = count
        return self.http.get(URL, params=params)

    def get_days_candles(self, market, to=None, count=None):
        '''
        일(Day) 캔들
        https://docs.upbit.com/v1.0/reference#%EC%9D%BCday-%EC%BA%94%EB%93%A4-1
        :param str market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param str to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX. 비워서 요청시 가장 최근 캔들
        :param int count: 캔들 개수
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/candles/days'
        params = {'market': market}
        if to is not None:
            params['to'] = to
        if count is not None:
            params['count'] = count
        return self.http.get(URL, params=params)

    def get_weeks_candles(self, market, to=None, count=None):
        '''
        주(Weeks) 캔들
        https://docs.upbit.com/v1.0/reference#%EC%A3%BCweek-%EC%BA%94%EB%93%A4-1
        :param str market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param str to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX. 비워서 요청시 가장 최근 캔들
        :param int count: 캔들 개수
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/candles/weeks'
        params = {'market': market}
        if to is not None:
            params['to'] = to
        if count is not None:
            params['count'] = count
        return self.http.get(URL, params=params)

    def get_months_candles(self, market, to=None, count=None):
        '''
        월(Months) 캔들
        https://docs.upbit.com/v1.0/reference#%EC%9B%94month-%EC%BA%94%EB%93%A4-1
        :param str market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param str to: 마지막 캔들 시각 (exclusive). 포맷 : yyyy-MM-dd'T'HH:mm:ssXXX. 비워서 요청시 가장 최근 캔들
        :param int count: 캔들 개수
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/candles/months'
        params = {'market': market}
        if to is not None:
            params['to'] = to
        if count is not None:
            params['count'] = count
        return self.http.get(URL, params=params)

    def get_trades_ticks(self, market, to=None, count=None, cursor=None):
        '''
        당일 체결 내역
        https://docs.upbit.com/v1.0/reference#%EC%8B%9C%EC%84%B8-%EC%B2%B4%EA%B2%B0-%EC%A1%B0%ED%9A%8C
        :param str market: 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :param str to: 마지막 체결 시각. 형식 : [HHmmss 또는 HH:mm:ss]. 비워서 요청시 가장 최근 데이터
        :param int count: 체결 개수
        :param str cursor: 페이지네이션 커서 (sequentialId)
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/trades/ticks'
        params = {'market': market}
        if to is not None:
            params['to'] = to
        if count is not None:
            params['count'] = count
        if cursor is not None:
            params['cursor'] = cursor
        return self.http.get(URL, params=params)

    def get_ticker(self, markets):
        '''
        현재가 정보
        요청 당시 종목의 스냅샷을 반환한다.
        https://docs.upbit.com/v1.0/reference#%EC%8B%9C%EC%84%B8-ticker-%EC%A1%B0%ED%9A%8C
        :param str[] markets: 반점으로 구분되는 마켓 코드 (ex. KRW-BTC, BTC-BCC)
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/ticker'
        if not isinstance(markets, list):
            raise InvalidParamException(
                'invalid parameter: markets should be list')

        if len(markets) == 0:
            raise InvalidParamException('invalid parameter: no markets')

        markets_data = markets[0]
        for market in markets[1:]:
            markets_data += ',%s' % market
        params = {'markets': markets_data}
        return self.http.get(URL, params=params)

    def get_orderbook(self, markets):
        '''
        호가 정보 조회
        https://docs.upbit.com/v1.0/reference#%ED%98%B8%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C
        :param str[] markets: 마켓 코드 목록 (ex. KRW-BTC,KRW-ADA)
        :return: json array
        '''
        URL = 'https://api.upbit.com/v1/orderbook?'
        if not isinstance(markets, list):
            raise InvalidParamException(
                'invalid parameter: markets should be list')

        if len(markets) == 0:
            raise InvalidParamException('invalid parameter: no markets')

        markets_data = markets[0]
        for market in markets[1:]:
            markets_data += ',%s' % market
        params = {'markets': markets_data}
        return self.http.get(URL, params=params)
