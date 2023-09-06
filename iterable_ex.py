# import re
# import reprlib

# rgx = re.compile('\w+')

# class Sentence:
#     def __init__(self, text):
#         self.text = text
#         self.word = rgx.findall(text)

#     def __getitem__(self, index):
#         return self.word[index]
    
#     def __len__(self):
#         return len(self.word)
    
#     def __repr__(self):
#         return 'Sentence(%s)' % reprlib.repr(self.text)

#     # def __iter__(self):
#     #     return (i for i in self.word)

# obj = Sentence("My name is Amardip Kumar")
# for i in obj:
#     print (i)

#------------


class Iterator(Iterable):
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self
    
    @classmethod
    def __subclasshook__(cls, C): 
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and any("__iter__" in B.__dict__ for B in C.__mro__)): 
                return True
        return NotImplemented

