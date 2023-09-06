

import collections.abc

def update(d, u):
    key = 'levelB'
    val = 10
    for k, v in d.items():
        if k != key:
            if isinstance(v, collections.abc.Mapping): 
                d[k] = update(d.get(k, {}), v)
        else:     
            d[k] = 10
    
    return d
dictionary1={'level1':{'level2':{'levelA':0,'levelB':1}}}
print (update(dictionary1, {'levelB': 10}))


# dict1 = {'level1' : 
#                 [
#                     {'level2': 
#                         [
#                             {'level3': 2}, {'level3_1': 3}
#                         ]
#                     }
#                 ],
#             'level4': [10],
#             'level5' : 
#                         [
#                           {  'level6' : 
#                                         [
#                                             {
#                                                 'level7': [5]
#                                             }
#                                         ]
#                           }

#                         ]

#         }