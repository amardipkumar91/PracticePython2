import pandas as pd
or_data = pd.read_csv('or.txt')
data = pd.read_csv('ee.csv')
data['Trade Reference Number'] = or_data['Trade Reference Number']
data['NCM ID'] = or_data['NCM ID']
data['Transferor'] = or_data['Transferor']
data['Transferee'] = or_data['Transferee']
data['Remaining Party '] = or_data['Remaining Party ']
data.to_csv("ee.csv")



