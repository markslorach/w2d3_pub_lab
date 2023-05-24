class Pub:
    def __init__(self,name, till, stock):
        self.name = name
        self.till = till
        self.stock = stock

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        return customer.age >= 18
    
    def check_stock_value(self):
        total = 0
        for drink in self.stock:
            total += (drink["stock"] * drink["price"])
        return total