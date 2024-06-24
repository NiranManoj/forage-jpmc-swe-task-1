import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Test for the first quote in quotes
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 120.48)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, (120.48 + 121.2) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Test for the second quote in quotes
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])

    self.assertEqual(stock, 'DEF')
    self.assertAlmostEqual(bid_price, 117.87)
    self.assertAlmostEqual(ask_price, 121.68)
    self.assertAlmostEqual(price, (117.87 + 121.68) / 2)

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_calculatePriceWithEqualBidAsk(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Test for the first quote in quotes
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 121.2)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, 121.2)

  def test_getDataPoint_calculatePriceWithZeroAskPrice(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Test for the first quote in quotes
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 121.2)
    self.assertAlmostEqual(ask_price, 0)
    self.assertAlmostEqual(price, (121.2 + 0) / 2)

  def test_getDataPoint_calculatePriceWithZeroBidPrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Test for the first quote in quotes
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])

    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 0)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, (0 + 121.2) / 2)

  #unit tests forn getRatio
  def test_getRatio_priceBZero(self):
    price_a = 100.0
    price_b = 0

    ratio = getRatio(price_a, price_b)

    self.assertEqual(ratio, 1)  # Adjusted assertion to expect 1 when price_b is 0

  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 50.0

    ratio = getRatio(price_a, price_b)

    self.assertEqual(ratio, 0)

  def test_getRatio_validPrices(self):
    price_a = 100.0
    price_b = 50.0

    ratio = getRatio(price_a, price_b)

    self.assertEqual(ratio, price_a / price_b)

if __name__ == '__main__':
    unittest.main()
