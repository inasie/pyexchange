# -*- coding: utf-8 -*-
import time


class OrderbookItem:
    """
    an orderbook item
    """

    def __init__(self, price, amount):
        '''
        constructor
        :param float price: price
        :param float amout: amount
        '''
        self._price = price
        self._amount = amount

    def __str__(self):
        return 'price: %.5f, amount: %.5f' % (self.price, self.amount)

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount


class Orderbook:
    """
    orderbook information
    """

    def __init__(self, currency_pair, asks, bids, timestamp=None):
        '''
        constructor
        :param CurrencyPair currency_pair: currency pair
        :param OrderbookItem[] asks: ask list
        :param OrderbookItem[] bids: bid list
        :param long timestamp: updated time
        '''
        self._currency_pair = currency_pair
        self._asks = asks
        self._bids = bids

        if timestamp is None:
            self._timestamp = int(time.time())
        else:
            self._timestamp = timestamp

    def __str__(self):
        _str = 'Orderbook(%s)-(%s)\n' % (str(self.timestamp),
                                         self.currency_pair)
        _str += 'Asks - \n'
        for ask in self.asks:
            _str += '\t%s\n' % ask
        _str += 'Bids - \n'
        for bid in self.bids:
            _str += '\t%s\n' % bid
        return _str

    @property
    def currency_pair(self):
        return self._currency_pair

    @property
    def asks(self):
        return self._asks

    @property
    def bids(self):
        return self._bids

    @property
    def timestamp(self):
        return self._timestamp
