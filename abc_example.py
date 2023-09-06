import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Test(collections.MutableSequence):
    ranks = [ str(n) for n in range(2, 11) + list('JQKA')]
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit ) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)


obj = Test()

import random 
class BingoCage:
    def __init__(self, items): 
        self._items = list(items) 
        random.shuffle(self._items)
    def pick(self): 
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage') 
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
import pdb;pdb.set_trace()
