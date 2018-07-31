import logging
from exchange.upbit.exchange_upbit import ExchangeUpbit
from exchange.bitflyer.exchange_bitflyer import ExchangeBitflyer
from exchange.bithumb.exchange_bithumb import ExchangeBithumb
from exchange.coinone.exchange_coinone import ExchangeCoinone
from exchange.bitfinex.exchange_bitfinex import ExchangeBitfinex
from exchange.okex.exchange_okex import ExchangeOKEx
from exchange.binance.exchange_binance import ExchangeBianace
from exchange.huobi.exchange_huobi import ExchangeHuobi
from exchange.gopax.exchange_gopax import ExchangeGopax
from exchange.zb.exchange_zb import ExchangeZB


class ExchangeAPI:
    EXCHANGES = ['Bitflyer', 'Bithumb', 'Bitfinex', 'Binance',
                 'Coinone', 'Gopax', 'Huobi', 'OKEx', 'Upbit', 'ZB']

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

        if exchange_name.__eq__('Bitflyer'):
            return ExchangeBitflyer()
        elif exchange_name.__eq__('Bithumb'):
            return ExchangeBithumb()
        elif exchange_name.__eq__('Bitfinex'):
            return ExchangeBitfinex()
        elif exchange_name.__eq__('Binance'):
            return ExchangeBianace()
        elif exchange_name.__eq__('Coinone'):
            return ExchangeCoinone()
        elif exchange_name.__eq__('Gopax'):
            return ExchangeGopax()
        elif exchange_name.__eq__('Huobi'):
            return ExchangeHuobi()
        elif exchange_name.__eq__('OKEx'):
            return ExchangeOKEx()
        elif exchange_name.__eq__('Upbit'):
            return ExchangeUpbit()
        elif exchange_name.__eq__('ZB'):
            return ExchangeZB()
        else:
            logging.error('invalid exchange: %s' % exchange_name)
            return NotImplementedError()
