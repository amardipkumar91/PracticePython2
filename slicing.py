class MySlice:
    def __getitem__(self, index):
        return index

obj = MySlice()
print (obj[1])
print (obj[1:4])