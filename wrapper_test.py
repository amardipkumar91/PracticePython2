from functools import wraps

def display_arguments(func):
    @wraps(func)
    def display_and_call(*args, **kwargs):      
        args = list(args)
        print('must-have arguments are:')
        for i in args:
            print(i)          
        print('optional arguments are:')
        for kw in kwargs.keys():
            print( kw+'='+str( kwargs[kw] ) )          
        return func(*args, **kwargs)   
    return display_and_call

@display_arguments
def my_add(m1, p1=0, p2=0):
    output_dict = {}
    output_dict['r1'] = m1+p1 + p2
    return output_dict

@display_arguments
def my_deduct(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1-p1
    return output_dict 
# import pdb;pdb.set_trace()
# print my_add(100,p1=1, p2= 20) 
obj = my_add.__wrapped__
print (obj(100,p1=1, p2= 20))