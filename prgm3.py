import pandas as pd
df = pd.read_csv('data.csv')
dup=df.duplicated().sum()
print('Number of Duplicated rows:',dup)
print('Number of rows in dataframe:',df.shape)
df_new = df
df_new=df_new.drop_duplicates()
dup1=df_new.duplicated().sum()
print('Number of duplicate rows after deleting duplicate values:',dup1)
print('Number of rows in dataframe:',df_new.shape)
