import pandas as pd
from pandasgui import show

data = {
    'Id': [101, 102, 103, 104, 105],
    'Name': ['ศุภชัย', 'สมใจ', 'ศักดิ์ชัย', 'พรชัย', 'ดวงใจ'],
    'Salary': [20000, 22000, 17000, 18500, 17900],
    'Age': [35, 30, 34, 27, 24]
}

df = pd.DataFrame(data)
show(df)
