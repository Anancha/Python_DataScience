import pandas as pd
import xlsxwriter
 
df = pd.DataFrame(
    {
        'ProductCost' : [80, 220, 240],
        'ProductPrice' : [100, 250, 280]            
    }
)

writer = pd.ExcelWriter('newproduct.xlsx', engine='xlsxwriter') 
df.to_excel(writer, sheet_name='สินค้า')
writer.save()