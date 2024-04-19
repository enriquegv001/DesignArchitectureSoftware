import logging

class FourCheese:
    """Get price of Soda"""
    def __init__(self):
        self.price = {"big": 15, "medium": 10 , "small": 5}
 
    def localize(self, size):
        """change the message using size"""
        self.price = self.price.get(size,size)
    
    def __str__(self):
        return "FourCheese"

class Soda:
    """Get price of Soda"""
 
    def __init__(self):
        self.price = {"big": 12, "medium": 8 , "small": 3}
 
    def localize(self, size):
        """change the message using size"""
        self.price = self.price.get(size,size)
    
    def __str__(self):
        return "Soda"
    
class Chef:
    """Builder for pizza"""

    def __init__(self):
        self.pizza = None

    def select_product(self, pizza_type = FourCheese):
        self.pizza = pizza_type()
    
    def select_size(self, size = 'big'):
        self.pizza.localize(size)

    def __str__(self):
        return 'Order: {0} || Price: {0.price}'.format(self.pizza)

class BeverageTender:
    """Builder for beverage"""

    def __init__(self):
        self.beverage = None

    def select_product(self, beverage_type = Soda):
        self.beverage = beverage_type()
    
    def select_size(self, size = 'big'):
        self.beverage.localize(size)

    #def show_order(self):
    #    return f'Order: {self.beverage} || Price: {self.beverage.price}'

    def __repr__(self):
        return 'Order: {0} || Price: {0.price}'.format(self.beverage)

class DeliverOrder:
    """Director of orders"""

    def build(self, employee):
        employee.select_product()
        employee.select_size()
        return employee
    
if __name__ == "__main__":
    restaurant = DeliverOrder()
    chef = Chef()
    bt = BeverageTender()
    print(restaurant.build(chef))
    print(restaurant.build(bt))

    