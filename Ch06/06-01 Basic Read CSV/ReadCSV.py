import pandas as pd

uri = 'product.csv'
df = pd.read_csv(uri,encoding='utf-8')
print('------------------------------------')
print(type(df))
print(df)
