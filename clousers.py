# class Averager(object):
#     def __init__(self):
#         self.series = []
    
#     def __call__(self, new_value):
#         self.series.append(new_value)
#         total = sum(self.series)
#         return total / len(self.series)


#-------------------------------------Non Local Declaration Python3-----

def make_averager(): 
    count = 0
    total = 0
    def averager(new_value): 
        nonlocal count, total
        count += 1
        total += new_value 
        return total / count
    def sum():
        nonlocal count
        count += 5
        return count
        
    return averager, sum
    