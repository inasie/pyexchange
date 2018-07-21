import unittest
import logging
from exchange import CurrencyPair
from exchange import ExchangeAPI


class ExchangeBitfinexTest(unittest.TestCase):

    def get_exchange(self):
        exchange = ExchangeAPI()
        return exchange.create_exchange('Bitfinex')

    def test_get_currency_pairs(self):
        pairs = self.get_exchange().get_currency_pairs()
        self.assertIsNotNone(pairs)
        self.assertNotEqual(len(pairs), 0)
        for pair in pairs:
            self.assertIsNotNone(pair.base_currency)
            self.assertIsNotNone(pair.currency)
            logging.info(pair)

    def test_get_ticker(self):
        ticker = self.get_exchange().get_ticker(CurrencyPair('USD', 'BTC'))
        self.assertIsNotNone(ticker)
        logging.info(ticker)

    def test_get_orderbook(self):
        orderbook = self.get_exchange().get_orderbook(CurrencyPair('USD', 'ETH'))
        self.assertIsNotNone(orderbook)
        logging.info(orderbook)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
