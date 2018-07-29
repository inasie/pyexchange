# -*- coding: utf-8 -*-
class CurrencyPair:
    """
    Currency pair
    """

    def __init__(self, market_currency, currency):
        '''
        :param str market_currency: base currency
        :param str currency: target currency
        '''
        self._market_currency = market_currency
        self._currency = currency

    def __str__(self):
        return 'market_currency: %s, currency: %s' % (self._market_currency, self._currency)

    @property
    def market_currency(self):
        return self._market_currency

    @property
    def currency(self):
        return self._currency
