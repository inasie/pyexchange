# -*- coding: utf-8 -*-
import logging
from exchange.errors import *
from exchange.utils.http_util import HttpUtil


class Bithumb():
    """
    Bithumb
    https://www.bithumb.com/u1/US127
    """

    def __init__(self):
        self.http = HttpUtil()

    def ticker(self, currency):
        '''
        bithumb 거래소 마지막 거래 정보
        https://www.bithumb.com/u1/US127
        :param str currency: BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS, ICX, VEN, TRX, ELF, MITH, MCO, OMG, KNC, GNT, HSR, ZIL, ETHOS, PAY, WAX, POWR, LRC, GTO, STEEM, STRAT, ZRX, REP, AE, XEM, SNT, ADA (기본값: BTC), ALL(전체)
        :return: json object
        '''
        URL = 'https://api.bithumb.com/public/ticker/'
        return self.http.get(URL + currency)

    def orderbook(self, currency, group_orders=1, count=5):
        '''
        bithumb 거래소 판/구매 등록 대기 또는 거래 중 내역 정보
        https://www.bithumb.com/u1/US127
        :param str currency: BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS, ICX, VEN, TRX, ELF, MITH, MCO, OMG, KNC, GNT, HSR, ZIL, ETHOS, PAY, WAX, POWR, LRC, GTO, STEEM, STRAT, ZRX, REP, AE, XEM, SNT, ADA (기본값: BTC), ALL(전체)
        :param int group_orders: Value : 0 또는 1 (Default : 1)
        :param int count: Value : 1 ~ 50 (Default : 20), ALL : 1 ~ 5(Default : 5)
        :return: json object
        '''
        URL = 'https://api.bithumb.com/public/orderbook/'
        if group_orders not in [0, 1]:
            raise InvalidParamException(
                'invalid group_orders: %d' % group_orders)
        if count < 1 or count > 50:
            raise InvalidParamException('invalid count: %d' % count)
        params = {
            'group_orders': group_orders,
            'count': count
        }
        return self.http.get(URL + currency, params=params)

    def transaction_history(self, currency, cont_no=None, count=20):
        '''
        bithumb 거래소 거래 체결 완료 내역
        https://www.bithumb.com/u1/US127
        :param str currency: BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS, ICX, VEN, TRX, ELF, MITH, MCO, OMG, KNC, GNT, HSR, ZIL, ETHOS, PAY, WAX, POWR, LRC, GTO, STEEM, STRAT, ZRX, REP, AE, XEM, SNT, ADA (기본값: BTC)
        :param int cont_no: Value : 체결 번호
        :param int count: Value : 1 ~ 100 (Default : 20)
        :return: json object
        '''
        URL = 'https://api.bithumb.com/public/transaction_history/'
        if count < 1 or count > 100:
            raise InvalidParamException('invalid count: %d' % count)
        params = {'count': count}
        if cont_no != 0:
            params['cont_no'] = cont_no
        return self.http.get(URL + currency, params=params)
