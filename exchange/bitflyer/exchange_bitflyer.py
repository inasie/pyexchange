from exchange.errors import *
from exchange.ticker import Ticker
from exchange.orderbook import *
from exchange.currency_pair import CurrencyPair
from exchange.exchange_base import ExchangeBase
from exchange.bitflyer.bitflyer import Bitflyer


class ExchangeBitflyer(ExchangeBase):
    """
    Bitflyer
    """
    NAME = 'Bitflyer'
    VERSION = 'v1'
    URL = 'https://lightning.bitflyer.com/docs?lang=en'

    def __init__(self):
        super().__init__(self.NAME, self.VERSION, self.URL)
        self._bitflyer = Bitflyer()

    def get_currency_pairs(self):
        '''
        Gets currency list supported by exchange
        :return: supported currency pair list
        :rtype: CurrencyPair[]
        '''
        currency_pairs = []
        markets = self._bitflyer.get_markets()
        for market_obj in markets:
            market = market_obj['product_code']
            if len(market) != 7:
                continue
            currency = market[0:3]
            market_currency = market[4:]
            currency_pairs.append(CurrencyPair(market_currency, currency))
        return currency_pairs

    def get_ticker(self, currency_pair):
        '''
        Gets last price
        :param CurrencyPair currency_pair: currency pair
        :return: ticker
        :rtype: Ticker
        '''

        product_code = currency_pair.currency + '_' + currency_pair.market_currency
        ticker = self._bitflyer.get_ticker(product_code)
        price = float(ticker['ltp'])
        return Ticker(currency_pair, price)

    def get_orderbook(self, currency_pair):
        '''
        Gets orderbook information
        :param CurrencyPair currency_pair: currency pair
        :return: orderbook
        :rtype: Orderbook
        '''
        product_code = currency_pair.currency + '_' + currency_pair.market_currency
        orderbook = self._bitflyer.get_orderbook(product_code)

        bids = []
        for unit in orderbook['bids']:
            price = float(unit['price'])
            amount = float(unit['size'])
            bids.append(OrderbookItem(price, amount))
        asks = []
        for unit in orderbook['asks']:
            price = float(unit['price'])
            amount = float(unit['size'])
            asks.append(OrderbookItem(price, amount))
        return Orderbook(currency_pair, asks, bids)
