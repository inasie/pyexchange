import logging
from exchange.upbit.exchange_upbit import ExchangeUpbit
from exchange.bithumb.exchange_bithumb import ExchangeBithumb
from exchange.bitfinex.exchange_bitfinex import ExchangeBitfinex


class ExchangeAPI:
    EXCHANGES = ['Upbit', 'Bithumb', 'Bitfinex', 'Binance']

    def get_exchanges(self):
        '''
        Currently supported exchanges
        :return: exchange name list
        :rtype str[]
        '''
        return self.EXCHANGES

    def create_exchange(self, exchange_name):
        '''
        create an Exchange obj
        :param str exchange_name: an exchange name
        :return: Exchange object
        :rtype ExchangeBase
        '''

        if exchange_name.__eq__('Upbit'):
            return ExchangeUpbit()
        elif exchange_name.__eq__('Bithumb'):
            return ExchangeBithumb()
        elif exchange_name.__eq__('Bitfinex'):
            return ExchangeBitfinex()
        elif exchange_name.__eq__('Binance'):
            return ExchangeBitfinex()
        else:
            logging.error('invalid exchange: %s' % exchange_name)
            return NotImplementedError()
