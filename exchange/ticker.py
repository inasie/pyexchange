# -*- coding: utf-8 -*-
class Ticker:
    """
    last traded price
    """

    def __init__(self, currency_pair, price, timestamp):
        '''
        contructor
        :param CurrencyPair currency_pair: currency pair
        :param float price: price
        :param long timestamp: updated time
        '''
        self.currency_pair = currency_pair
        self.price = price
        self.timestamp = timestamp

    def __str__(self):
        return 'currency_pair: %s, price: %.2f, timestamp: %ld' % (self.currency_pair, self.price, self.timestamp)
