class FourCheese:
    """Get price FourCheese pizza"""
    def __init__(self):
        self.size = {"big": 15, "medium": 10 , "small": 5}
 
    def localize(self, price):
        """change the message using size"""
        return self.size.get(price, price)
 
class Pepperoni:
    """ Get price of Pepperoni"""
 
    def __init__(self):
        self.size = {"big": 12, "medium": 8 , "small": 3}
 
    def localize(self, price):
        """change the message using size"""
        return self.size.get(price, price)

 
def Factory(pizza_type ="Pepperoni"):
    """Factory Method"""
    pizzas = {
        "FourCheese": FourCheese,
        "Pepperoni": Pepperoni,
    }
 
    return pizzas[pizza_type]()
 
if __name__ == "__main__":
 
    f = Factory("FourCheese")
    p = Factory("Pepperoni")
 
    orders = ["big", "small", "medium"]
 
    for order in orders:
        print(f.localize(order))
        print(p.localize(order))