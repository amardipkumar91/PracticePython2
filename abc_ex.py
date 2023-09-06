import abc
import random
class Tambola(abc.ABC):

    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return 

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except:
                break
        self.load(items)
        return tuple(sorted(items))

# class BingoCage(Tambola):
#     def __init__(self, items):
#         self._items = []
#         self._randomizer = random.SystemRandom()
#         self.load(items)
        
#     def load(self, item):
#         self._items.append(item)
#         self._randomizer.shuffle(self._items)
    
#     def pick(self):
#         try:
#             return self._items.pop()
#         except:
#             raise LookupError("Empty")

#     def __call__(self):
#         return self.pick()
# obj = BingoCage(4)
# obj.load(5)
# obj.load(6)
# obj.load(7)
# print (obj())
        
class LotteryBlower(Tambola):
    def __init__(self, iterable):
        self._ball = list(iterable)
    
    def load(self, item):
        self._ball.append(item)

    def pick(self):
        try:
            position = random.randrange(len(self._ball))
        except:
            raise LookupError("Empty")
        return self._ball.pop(position)
    
    def loaded(self):
        return bool(self._ball)
    
    def inspect(self):
        return tuple(sorted(self._ball))

obj = LotteryBlower([5])
obj.load(6)
obj.load(7)
obj.load(8)
print (obj.pick())






