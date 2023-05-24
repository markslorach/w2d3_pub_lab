import unittest
from src.pub import Pub
from src.customer import Customer




class TestPub(unittest.TestCase):
    def setUp(self):
        stock = [{
                "name" : "Tennents",
                "stock": 20,
                "price": 5.00
            },
            {
                "name": "Malibu",
                "stock": 20,
                "price": 5.00
            },
            {
                "name": "Coke",
                "stock": 20,
                "price": 1.00
            }
        ]     
        self.pub = Pub("The Drum and Drone", 100.00, stock)

    def test_pub_has_name(self):
        self.assertEqual("The Drum and Drone", self.pub.name)

    def test_pub_has_till_value(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_has_drinks(self):
        self.assertEqual(3, len(self.pub.stock))

    def test_check_age(self):
        customer = Customer("Mark", 100.00, 31, 4)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_check_under_age(self):
        customer = Customer("Annie", 5000.00, 9, 0)
        self.assertEqual(False, self.pub.check_age(customer))

    def test_has_stock_value(self):  
        self.assertEqual(220,  self.pub.check_stock_value())
        