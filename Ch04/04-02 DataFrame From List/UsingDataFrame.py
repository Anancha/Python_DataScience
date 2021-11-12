import pandas as pd

data = [
        ['สมชาย', 185, 16000], ['วีระชัย', 175, 17500], 
        ['พรชัย', 182, 20000], ['วีระ', 183, 19900]
       ]

colsname = ['ชื่อ', 'ส่วนสูง', 'เงินเดือน']
df = pd.DataFrame(data, columns = colsname)

print('------------------------------------')
print(type(df))
print(df)
