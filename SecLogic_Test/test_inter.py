class A(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __display(self):
        return self.a
    
    def _dispaly(self):
        return self.b

    def foo(self):
        return self.a + self.b

class B(A):
    pass

obj = B()

Employee:-   select * from( select t1.Name, t3.salary, t2.departmentid from Employee as t1 left join EmpDepart as t2
                on t1.Id = t2.empid
                join EmploySalay as t3
                on t1.id = t3.EmpId order by t3.salary desc)
                group by t2.departmentid

Id
Name
Mobile
Email

EmpDepart
id
empid
departmentid

EmpDepartment:
id
departmentname

EmploySalay:
id
EmpId
salary