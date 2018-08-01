import logging
from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.coinbase.coinbase_pro import CoinbasePro


class ExchangeCoinbasePro(ExchangeBase):
    """
    Coinbase Pro
    """
    NAME = 'Coinbase Pro'
    VERSION = 'Unknown'
    URL = 'https://docs.pro.coinbase.com'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._coinbase_pro = CoinbasePro()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        products = self._coinbase_pro.get_products()

        for product_obj in products:
            market_currency = product_obj['quote_currency']
            currency = product_obj['base_currency']
            currency_pairs.append(CurrencyPair(market_currency, currency))
        return currency_pairs

    def get_ticker(self, currency_pair):
        '''
        Gets last price
        :param CurrencyPair currency_pair: currency pair
        :return: ticker
        :rtype: Ticker
        '''
        if currency_pair is None:
            raise InvalidParamException('currency_pair is None')
        id = currency_pair.currency + '-' + currency_pair.market_currency
        ticker = self._coinbase_pro.get_product_ticker(id)
        price = float(ticker['price'])
        return Ticker(currency_pair, price)

    def get_orderbook(self, currency_pair):
        '''
        Gets orderbook information
        :param CurrencyPair currency_pair: currency pair
        :return: orderbook
        :rtype: Orderbook
        '''
        if currency_pair is None:
            raise InvalidParamException('currency_pair is None')
        id = currency_pair.currency + '-' + currency_pair.market_currency
        orderbook = self._coinbase_pro.get_product_order_book(id, level=2)

        asks = []
        for unit in orderbook['asks']:
            price = float(unit[0])
            amount = float(unit[1])
            asks.append(OrderbookItem(price, amount))

        bids = []
        for unit in orderbook['bids']:
            price = float(unit[0])
            amount = float(unit[1])
            bids.append(OrderbookItem(price, amount))

        return Orderbook(currency_pair, asks, bids)
