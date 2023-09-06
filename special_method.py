#----------------collection namedtuple---------------------------------
#---------- A deck as a sequence of cards.---------------------------

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position): 
        return self._cards[position]

beer_card = Card('7', 'diamonds')
deck = FrenchDeck()

suit_values = dict(spades=0, hearts=1, diamonds=2, clubs=3)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key = spades_high):
    print (card)

# ---- Vector class implementing the operations just described, through the use of the special methods __repr__, __abs__, __add__ and __mul__:---------

from math import hypot
class Vector:
    def __init__(self, x =0 , y= 0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "Vector(%r, %r)"%(self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scaler):
        return Vector(self.x * scaler , self.y * scaler)
    
obj = Vector(4,5)
import pdb;pdb.set_trace()


#----------------Name Tuple --------------

# from collections import namedtuple
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# import pdb;pdb.set_trace()
# print (tokyo.country)
# print (tokyo.population)

# LatLong = namedtuple('LatLong', 'lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# delhi = City._make(delhi_data)
# print ( delhi._asdict())


#-----------------DefaultDict-------------
import sys
import re
import collections
WORD_RE = re.compile('\w+')
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index[word].append(location)





    


