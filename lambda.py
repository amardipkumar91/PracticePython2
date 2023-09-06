# find max len of str in a list

# # 1 way
# data = ['amar', 'vicky', 'amardip']
# print (reduce(lambda x, y : x if len(x) > len(y) else y, data))

# #2 way
# print (max(data, key=len))


file_path = '/Users/amardip.kumar/Downloads/CI words.xlsx'
from pandas import DataFrame
import pandas as pd
data = {}
df = pd.read_excel(file_path)
df_dict = df.to_dict()
keyword = df_dict['Keyword']
ci = df_dict['CI']
for i,j in keyword.iteritems():
    data.update({ j : ci[i]})


add_file_path = '/Users/amardip.kumar/Desktop/test.xlsx'
df1 = pd.read_excel(add_file_path)
index_val = df1[df1['Keyword'].str.contains('a')].index.tolist()
if index_val:
    index_val = index_val
    for i in index_val:
        df1.loc[i, 'news'] = 'flag'
df1.to_excel(add_file_path)

