import openpyxl as xl

wb = xl.Workbook()
ws = wb.worksheets[0]

for i in range(10):
    ws.cell(i+1, 1).value = (i+1)*100
wb.save('data.xlsx')
print('สร้างไฟล์ Excel เสร็จเรียบร้อยแล้ว')

