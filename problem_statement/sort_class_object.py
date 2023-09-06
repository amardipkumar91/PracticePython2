# import random
# def main(len_of_list):
#     lst= []
#     if len_of_list < 500 and len_of_list > 100:
#         lst_len = len_of_list
#         count = 0
#         while True:
#             lst.append(random.choice(range(1,100)))
#             count = count + 1
#             if count == len_of_list:
#                 break
#     print sorted(lst)
    
# main(random.choice(range(100,500)))

class Student(object):
    def __init__(self, name, gender, cls, section, marks):
        self.name = name
        self.gender = gender
        self.cls = cls
        self.section = section
        self.marks = marks
    
pbj = Student('Amar', 'M', 10, 'A', 100)
pbj1 = Student('Vicky', 'M', 10, 'A', 300)
pbj2 = Student('Amar1', 'M', 10, 'A', 105)
pbj3 = Student('Amar2', 'M', 10, 'B', 110)
pbj4 = Student('Amar3', 'M', 10, 'B', 115)
lst = [pbj, pbj1, pbj2, pbj3, pbj4]
print (lst)
for i in lst:
    print (i.marks)
def sort_marks(student):
    return student.marks

sorted_student_marks = sorted(lst, key = sort_marks)
for i in sorted_student_marks:
    print (i.marks)
    
