import unittest
import logging
from exchange.currency_pair import CurrencyPair
from exchange.exchange_api import ExchangeAPI


class ExchangeBithumbTest(unittest.TestCase):

    def test_get_currency_pairs(self):
        exchange = ExchangeAPI()
        upbit = exchange.create_exchange('Bithumb')
        pairs = upbit.get_currency_pairs()
        self.assertIsNotNone(pairs)
        self.assertNotEqual(len(pairs), 0)
        for pair in pairs:
            self.assertIsNotNone(pair.base_currency)
            self.assertIsNotNone(pair.currency)
            logging.info(pair)

    def test_get_ticker(self):
        exchange = ExchangeAPI()
        upbit = exchange.create_exchange('Bithumb')
        ticker = upbit.get_ticker(CurrencyPair('KRW', 'ICX'))
        self.assertIsNotNone(ticker)
        logging.info(ticker)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()
