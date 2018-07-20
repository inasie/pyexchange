import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bithumb.bithumb import Bithumb


class ExchangeBithumb(ExchangeBase):
    """
    빗썸
    """
    NAME = 'Bithumb'
    VERSION = '1.0'
    URL = 'https://www.bithumb.com/u1/US127'

    def __init__(self):
        '''
        생성자
        '''
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.bithumb = Bithumb()

    def get_currency_pairs(self):
        '''
        지원되는 암호화폐 쌍 리스트
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        ticker_all = self.bithumb.ticker('ALL')
        if int(ticker_all['status']) != 0:
            raise Exception('ticker() failed(%s)' % ticker_all['status'])
        for key in ticker_all['data'].keys():
            if key == 'date':
                continue
            currency_pairs.append(CurrencyPair("KRW", key.upper()))
        return currency_pairs

    def get_ticker(self, currency_pair):
        '''
        암호화폐쌍의 Ticker 정보 얻기
        :param CurrencyPair currency_pair: 암호화폐 쌍
        :return: ticker 정보
        :rtype: Ticker
        '''
        if currency_pair is None:
            raise InvalidParamException('currency_pair is None')
        if currency_pair.base_currency != 'KRW':
            raise InvalidParamException('invalid base_currency')
        ticker = self.bithumb.ticker(currency_pair.currency)
        if int(ticker['status']) != 0:
            raise Exception('ticker() failed(%s)' % ticker['status'])
        price = float(ticker['data']['closing_price'])
        timestamp = int(ticker['data']['date'])
        return Ticker(currency_pair, price, timestamp)
