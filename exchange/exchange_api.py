import logging
from exchange.upbit.exchange_upbit import ExchangeUpbit
from exchange.bithumb.exchange_bithumb import ExchangeBithumb


class ExchangeAPI:
    EXCHANGES = ['Upbit', 'Bithumb']

    def get_exchanges(self):
        '''
        지원되는 거래소 리스트
        :return: 거래소 문자열 리스트
        :rtype str[]
        '''
        return self.EXCHANGES

    def create_exchange(self, exchange_name):
        '''
        거래소 객체 생성
        :param str exchange_name: 거래소 이름
        :return: 거래소 객체
        :rtype ExchangeBase
        '''

        if exchange_name.__eq__('Upbit'):
            return ExchangeUpbit()
        elif exchange_name.__eq__('Bithumb'):
            return ExchangeBithumb()
        else:
            logging.error('invalid exchange: %s' % exchange_name)
            return NotImplementedError()
