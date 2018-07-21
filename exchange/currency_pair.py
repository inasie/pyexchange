# -*- coding: utf-8 -*-
class CurrencyPair:
    """
    Currency pair
    """

    def __init__(self, base_currency, currency):
        '''
        :param str base_currency: base currency
        :param str currency: target currency
        '''
        self.base_currency = base_currency
        self.currency = currency

    def __str__(self):
        return 'base_currency: %s, currency: %s' % (self.base_currency, self.currency)
