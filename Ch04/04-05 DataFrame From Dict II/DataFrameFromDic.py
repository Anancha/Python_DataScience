import pandas as pd

person = ["สมศรี", "พิมพ์พร", "สุดใจ", "สมหญิง"]
height = [160, 166, 163, 168]
age = [25, 23, 27, 19]

data = {
            'ชื่อ':person,
            'ส่วนสูง':height,
            'อายุ':age
       }

df = pd.DataFrame(data)
print('------------------------------------')
print(type(data))
print(df)
