class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if self.radius < 0:
            raise ValueError("radius should not be less than 0")
        else:
            self._radius = radius
    
    @property
    def area(self):
        return 3.14 *self.radius ** 2
    


circle = Circle(2)
print (circle.area)

circle.radius = 10
print (circle.area)

