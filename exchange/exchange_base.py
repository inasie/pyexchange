# -*- coding: utf-8 -*-
class ExchangeBase:
    """
    거래소 기본 클래스
    """

    def __init__(self, name, version, url=None):
        '''
        생성자
        :param str name:거래소 이름
        :param str version: API version
        :param str url: API url
        '''
        self.name = name
        self.version = version
        self.url = url

    def get_currency_pairs(self):
        '''
        지원되는 암호화폐 쌍 리스트
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        return NotImplementedError()

    def get_ticker(self, currency_pair):
        '''
        암호화폐쌍의 Ticker 정보 얻기
        :param CurrencyPair currency_pair: 암호화폐 쌍
        :return: ticker 정보
        :rtype: Ticker
        '''
        return NotImplementedError()
