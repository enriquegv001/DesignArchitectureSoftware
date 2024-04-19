import random
 
class Pizza_At_Order:
    """ GeeksforGeeks portal for pizzas """
    def __init__(self, pizza_factory = None):
        """PizzaFactory is out abstract factory"""
        self.pizza_factory = pizza_factory
 
    def show_pizza(self, size = 'big'):
        """creates and show pizza using the abstract factory"""
        pizza = self.pizza_factory()
        print(f'Your order: {size} pizza of {pizza}')
        print(f'its price is {pizza.localize(size)}')

 

class FourCheese:
    """Get price of Pepperoni"""
    def __init__(self):
        self.size = {"big": 15, "medium": 10 , "small": 5}
 
    def localize(self, price):
        """change the message using size"""
        return self.size.get(price, price)
    
    def __str__(self):
        return "FourCheese"

class Pepperoni:
    """Get price of Pepperoni"""
 
    def __init__(self):
        self.size = {"big": 12, "medium": 8 , "small": 3}
 
    def localize(self, price):
        """change the message using size"""
        return self.size.get(price, price)
    
    def __str__(self):
        return "Pepperoni"
 
def Factory(pizza_type ="Pepperoni"):
    """Factory Method"""
    pizzas = {
        "FourCheese": FourCheese,
        "Pepperoni": Pepperoni,
    }
 
    return pizzas[pizza_type]()

def random_pizza():
    """A random function for selecting pizza"""
    return random.choice([FourCheese, Pepperoni])() 

def random_size():
    """A random function for selcting size"""
    return random.choice(['big', 'medium', 'small'])

if __name__ == "__main__":
    pizza = Pizza_At_Order(random_pizza)
 
    for i in range(5):
        pizza.show_pizza(random_size())