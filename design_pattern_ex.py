#Implementation Order class with pluggable discount strategies.
from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')


class ListItem(object):
    def __init__(self, product, qunatity, price):
        self.product = product
        self.qunatity = qunatity
        self.price = price

    def total(self):
        return self.price * self.qunatity

class Promotion(ABC):
    @abstractmethod
    def discount(self):
        pass
        

class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.qunatity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart} 
        if len(distinct_items) >= 10:
            return order.total() * .07 
        return 0

# promos = [FidelityPromo.discount, BulkItemPromo.discount, LargeOrderPromo.discount]
class Order(object):
    def __init__(self, customer, cart, promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>' 
        return fmt.format(self.total(), self.due())

    
if __name__ == '__main__':

    joe = Customer('John Doe', 1900)
    ann = Customer('Ann Smith', 1100)
    cart = [ListItem('banana', 39, .5),ListItem('apple', 10, 1.5),ListItem('watermellon', 5, 5.0)]
    obj = Order(joe, cart, FidelityPromo())

    obj1 = Order(ann, cart, FidelityPromo())
    print (obj)
    # print (obj.best_promo())



