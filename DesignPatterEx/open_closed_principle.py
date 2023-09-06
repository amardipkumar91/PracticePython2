from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# OCP : open for extension not for modification . it does not scale
class ProductFilter:
    def filter_by_color(self, product, color):
        for p in product:
            if p.color == color:
                yield p
                
    def filter_by_size(self, product, size):
        for p in product:
            if p.size == size: yield p
    
    def filter_by_size_and_color(self, product, color, size):
        for p in product:
            if p.size == size and p.color == p.color: yield p

# Specification

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpectification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpectification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        return all(map(
            lambda spec : spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    product = [apple, tree, house]
    pf = ProductFilter()
    print (f"Green Product: Old")
    for p in pf.filter_by_color(product, Color.GREEN):
        print (f" - {p.name} is green")

    print (f"Green Product: New approach")
    bf = BetterFilter()
    green = ColorSpectification(Color.GREEN)
    for p in bf.filter(product, green):
        print (f" - {p.name} is green")
    
    print (f"Large Product")
    large = SizeSpectification(Size.LARGE)
    for p in bf.filter(product, large):
        print (f" - {p.name} is large")
    
    print ("Large Blue items")
    #large_blue = AndSpecification(large, ColorSpectification(Color.BLUE))
    large_blue = large & ColorSpectification(Color.BLUE)
    for p in bf.filter(product, large_blue):
        print (f" - {p.name} is large and blue")


