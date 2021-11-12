import pandas as pd

male = ['สมชาย', 'วีระชัย', 'พรชัย', 'วีระ']
heightmale = [180, 183, 185, 184]

data = list(zip(male, heightmale))

colsname = ['ชื่อ','ส่วนสูง']
df = pd.DataFrame(data, columns=colsname)

print('------------------------------------')
print(type(df))
print(df)
