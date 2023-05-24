import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Mark", 100.00, 31, 4)

    def test_customer_has_name(self):
        self.assertEqual("Mark", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(31, self.customer.age)

    def test_customer_can_buy_drink(self):
        drinks = ["Tennents", "Malibu", "Coke"]
        drink = Drink("Tennents", 5.00, 4)
        pub = Pub("The Drum and Drone", 100.00, drinks)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(95.00, self.customer.wallet)
        self.assertEqual(105.00, pub.till)

    def test_customer_has_had_drink(self):
        drink = Drink("Tennents", 5.00, 4)
        self.customer.has_had_drink(drink)
        self.assertEqual(8, self.customer.drunkeness)

    def test_customer_has_had_food(self):
        food = Food("Burger", 5.00, 4)
        self.customer.buy_food(food)
        self.assertEqual(95.00, self.customer.wallet)
        self.assertEqual(0, self.customer.drunkeness)
 