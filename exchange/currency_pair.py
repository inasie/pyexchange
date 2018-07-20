# -*- coding: utf-8 -*-
class CurrencyPair:
    """
    암호화폐 쌍 클래스
    """

    def __init__(self, base_currency, currency):
        '''
        :param str base_currency: 기축 화폐(코인/화폐)
        :param str currency: 거래 대상 화폐
        '''
        self.base_currency = base_currency
        self.currency = currency

    def __str__(self):
        return 'base_currency: %s, currency: %s' % (self.base_currency, self.currency)
