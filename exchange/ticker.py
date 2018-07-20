# -*- coding: utf-8 -*-
class Ticker:
    """
    Ticker 정보
    """

    def __init__(self, currency_pair, price, timestamp):
        '''
        생성자
        :param CurrencyPair currency_pair: Ticker 정보의 암호화폐 쌍
        :param float price: 가격
        :param long timestamp: 업데이트 시간
        '''
        self.currency_pair = currency_pair
        self.price = price
        self.timestamp = timestamp

    def __str__(self):
        return 'currency_pair: %s, price: %.2f, timestamp: %ld' % (self.currency_pair, self.price, self.timestamp)
