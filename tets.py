import pandas as pd

dfUser_info = pd.read_csv('./data/cleanCSV/user_info.csv', index_col=0)
dfUser_info = dfUser_info.groupby('MAC').size()
print(dfUser_info)


duplicate_values = dfUser_info['MAC'].duplicated()
print(duplicate_values)