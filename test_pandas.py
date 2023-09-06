file_path = '/Users/amardip.kumar/Downloads/CI words.xlsx'
from pandas import DataFrame
import pandas as pd
data = {}
df = pd.read_excel(file_path)
import pdb;pdb.set_trace()
df_dict = df.to_dict()
keyword = df_dict['Keyword']
ci = df_dict['CI']
for i,j in keyword.iteritems():
    data.update({ j : ci[i]})

    