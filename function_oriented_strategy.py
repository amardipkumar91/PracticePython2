from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class ListItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

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
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>' 
        return fmt.format(self.total(), self.due())

promos = []
def promotion(promos_func):
    promos.append(promos_func)

@promotion
def fidelity_promo(order):
    # import pdb;pdb.set_trace()
    """5% discount for customers with 1000 or more fidelity points""" 
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units""" 
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order_promo(order):
    
    
    """7% discount for orders with 10 or more distinct items""" 
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
   
    """Select best discount available
    """
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 1000)
ann = Customer('Ann Smith', 1100)
cart = [ListItem('banana', 4, .5),ListItem('apple', 10, 1.5),ListItem('watermellon', 5, 5.0)]
obj = Order(joe, cart, fidelity_promo)
import pdb;pdb.set_trace()
# print ("------------")
# print (obj)
# print ("------------")
# obj1 = Order(ann, cart, large_order_promo)
# print (obj1)
# banana_cart = [ListItem('banana', 30, .5),ListItem('apple', 10, 1.5)]
# obj2 = Order(joe, banana_cart, bulk_item_promo)
# print (obj2)
# long_order = [ListItem(str(item_code), 1, 1.0) for item_code in range(10)]
# obj3 = Order(ann, long_order, large_order_promo)
# print (obj3)
# print ("---")
# obj4 = Order(joe, long_order, best_promo)
# print ("---")
# print (obj4)