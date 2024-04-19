import logging

class Pizza:

    def __init__(self, pizza_type = None):
        self.type = pizza_type
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def deliver_order(self):
        if self.type is not None:
            self.logger.info(f'Your pizza order is {self.type}')
        else:
            self.logger.info('No pizza type specified')

    def clone(self, pizza_type):
        return Pizza(pizza_type)

if __name__ == "__main__":
    pizzaPrototype = Pizza()
    ord1 = pizzaPrototype.clone('Pepperoni')
    ord2 = pizzaPrototype.clone('FourCheese')

    ord1.deliver_order()
    ord2.deliver_order()