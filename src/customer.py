class Customer:
    def __init__(self,name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def has_had_drink(self, drink):
        self.drunkeness += drink.alcohol_level

    def buy_drink(self, drink, pub):
        if pub.check_age(self) == True and self.drunkeness <= 20:
            if self.wallet >= drink.price:
                self.wallet -= drink.price
                pub.till += drink.price

    def buy_food(self, food):
        if self.wallet >= food.price:
            self.wallet -= food.price
            self.drunkeness -= food.rejuvination_level
        
