from exchange.errors import *
from exchange.ticker import Ticker
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.upbit.upbit import Upbit


class ExchangeUpbit(ExchangeBase):
    """
    업비트
    """
    NAME = 'Upbit'
    VERSION = '1.0'
    URL = 'https://docs.upbit.com/v1.0/reference'

    def __init__(self):
        '''
        생성자
        '''
        super().__init__(self.NAME, self.VERSION, self.URL)
        self.upbit = Upbit()

    def get_currency_pairs(self):
        '''
        지원되는 암호화폐 쌍 리스트
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        market_all = self.upbit.get_market_all()
        for market in market_all:
            tmp = market['market'].split('-')
            currency_pairs.append(CurrencyPair(tmp[0], tmp[1]))
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
        base_currency = currency_pair.base_currency
        currency = currency_pair.currency
        ticker = self.upbit.get_ticker(['%s-%s' % (base_currency, currency)])

        price = ticker[0]['trade_price']
        timestamp = ticker[0]['timestamp']
        return Ticker(currency_pair, price, timestamp)
