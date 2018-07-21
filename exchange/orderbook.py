# -*- coding: utf-8 -*-
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
        self.price = price
        self.amount = amount

    def __str__(self):
        return 'price: %.2f, amount: %.2f' % (self.price, self.amount)


class Orderbook:
    """
    orderbook information
    """

    def __init__(self, currency_pair, asks, bids, timestamp):
        '''
        constructor
        :param CurrencyPair currency_pair: currency pair
        :param OrderbookItem[] asks: ask list
        :param OrderbookItem[] bids: bid list
        :param long timestamp: updated time
        '''
        self.currency_pair = currency_pair
        self.asks = asks
        self.bids = bids
        self.timestamp = timestamp

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
