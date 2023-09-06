
# class Test(object):
#     def __init__(self, name):
#         self.name = name

#     @property 
#     def user_name(self):
#         return self.name
#     @user_name.setter
#     def user_name(self, name):
#         self.name = name + "**"

# class Test1(Test):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name)
#         self.last_name = last_name
    
#     def display(self):
#         return self.name + " " + self.last_name

# obj = Test1('amar', 'kumar')
# obj.user_name = "rahul"
# print (obj.display())
# import pdb;pdb.set_trace()

#---------------Manual GC -----
import gc, sys
i = 0
def make_cycle(i):
    x = {}
    x[i+1] = x

collected = gc.collect()
print ("collected objects:", collected)
for i in range(10):
    make_cycle(i)
collected = gc.collect()
print ("collected objects:", collected)


#-----
result = []
def foo(input_list):
    for i in input_list:
        if isinstance(i, list):
            # import pdb;pdb.set_trace()
            foo(i)
        else:
            result.append(i)
    return result
input_list = [1, 2, [3, 4, [5, 6] ], 7, 8, [9, [10] ] ]
print (foo(input_list))
    
# Find list is subset of other list in same order:
l1 = [1,2,3,4,5,6]
l2 = [1,2,4]
map_l1 = "".join(map(str, l1))
map_l2 = "".join(map(str, l2))
print (map_l2 in map_l1)
