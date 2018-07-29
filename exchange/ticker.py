# -*- coding: utf-8 -*-
import time


class Ticker:
    """
    last traded price
    """

    def __init__(self, currency_pair, price, timestamp=None):
        '''
        contructor
        :param CurrencyPair currency_pair: currency pair
        :param float price: price
        :param long timestamp: updated time
        '''
        self._currency_pair = currency_pair
        self._price = price
        if timestamp is None:
            self._timestamp = int(time.time())
        else:
            self._timestamp = timestamp

    def __str__(self):
        return 'currency_pair: %s, price: %.2f, timestamp: %ld' % (self.currency_pair, self.price, self.timestamp)

    @property
    def currency_pair(self):
        return self._currency_pair

    @property
    def price(self):
        return self._price

    @property
    def timestamp(self):
        return self._timestamp
