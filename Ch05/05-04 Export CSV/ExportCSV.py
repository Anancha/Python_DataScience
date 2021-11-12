import pandas as pd

df = pd.read_excel('Product.xlsx',
                   sheet_name='รายชื่อสินค้า')
result = df.to_csv(sep='#')
print(result)
