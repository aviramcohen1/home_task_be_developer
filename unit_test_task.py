import unittest
from Recursive_Digit_Summer import sum_of_digits
from Mistake_Cash import Price_Check

class MyTestCase(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(2347623),27)

    def test_correct_prices(self):
        products = ["apple", "orange", "banana"]
        productPrices = [1.50, 2.00, 1.00]
        productSold = ["apple", "orange", "banana"]
        soldPrice = [1.50, 2.00, 1.00]
        self.assertEqual(Price_Check(products, productPrices, productSold, soldPrice), 0)

    def test_incorrect_prices(self):
        products = ["apple", "orange", "banana"]
        productPrices = [1.50, 2.00, 1.00]
        productSold = ["apple", "orange", "banana"]
        soldPrice = [1.40, 2.00, 1.00]
        self.assertEqual(Price_Check(products, productPrices, productSold, soldPrice), 1)










if __name__ == '__main__':
    unittest.main()
