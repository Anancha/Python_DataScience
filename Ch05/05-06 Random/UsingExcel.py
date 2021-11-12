import openpyxl as xl
import numpy as np

wb = xl.Workbook()
ws = wb.worksheets[0]

for i in range(10):
    ws.cell(i+1, 1).value = np.random.randint(1000, 9999)
wb.save('data.xlsx')
print('สร้างไฟล์ Excel เสร็จเรียบร้อยแล้ว')

