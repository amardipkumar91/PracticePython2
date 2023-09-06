# def check_emp(request):
#     name = request.name
#     phone = request.phone

#     obj = Employee()
#     obj.name = name
#     obj.phone = phone
#     obj.save()

#     Employee.objects.order_by('-salary')[:10]



# input_str = 'Reverse this list word by word in python'
# result = " ".join (input_str.split()[::-1])

A = [3, 5, 9, 11, 13, 20, 21]
B= [2, 4, 8, 16,19]

len_A = len(A)
len_B = len(B)

# x,y = 0,0
# result= []
# while x < len_A and y< len_B:
#     if A[x] < B[y]:
#         result.append(A[x])
#         x = x + 1
#     else:
#         result.append(B[y])
#         y = y + 1

# result = result + A[x:] + B[y:]
# print (result)


class EmployeeIteraor:
    def __init__(self, employee):
        self.employee = employee
        self.index = 0

    def __next__(self):
        if self.index < len(self.employee.data_list):
            result =  self.employee.data_list[self.index]
            self.index += 1
            return result
        raise StopIteration

class EmployeeList:
    def __init__(self):
        self.data_list = list()
    def populate(self, a):
        self.data_list.append(a)
    
    def __iter__(self):
        return EmployeeIteraor(self)

    # def __next__(self):
    #     import pdb;pdb.set_trace()
    #     if self.index < len(self.data_list):
    #         result =  self.data[self.index]
    #         self.index += 1
    #     return result

obj = EmployeeList()
obj.populate('A')
obj.populate('A')
obj.populate('A')
iterator = iter(obj)
while True:
    try:
        elem = next(iterator)
        print (elem)
    except Exception as e:
        
        break


# class Team:
#     def __init__(self):
#        self._juniorMembers = list()
#        self._seniorMembers = list()
#     def addJuniorMembers(self, a):
#        self._juniorMembers += a
    
#     # def addSeniorMembers(self, a):
#     #    self._seniorMembers += a

#     def __iter__(self):
#        ''' Returns the Iterator object '''
#        return TeamIterator(self)

# class TeamIterator:
#    ''' Iterator class '''
#    def __init__(self, team):
#        self._team = team
#        self._index = 0

#    def __next__(self):
#         # if self._index < (len(self._team._juniorMembers) + len(self._team._seniorMembers)):
            
#         if self._index < len(self._team._juniorMembers):
#             result = (self._team._juniorMembers[self._index] , 'junior')
#             # else:
#             #     result = (self._team._seniorMembers[self._index - len(self._team._juniorMembers)]   , 'senior')
#             self._index +=1
#             return result
#         raise StopIteration
 
            
# team = Team()
# team.addJuniorMembers(['Sam', 'John', 'Marshal'])
# # team.addSeniorMembers(['Riti', 'Rani', 'Aadi'])
# iterator = iter(team)
# while True:
#     try:
#         elem = next(iterator)
#         print (elem)
#     except:
#         break

