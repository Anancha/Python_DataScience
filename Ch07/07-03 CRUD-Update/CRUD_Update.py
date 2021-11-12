import pyodbc

strConn = 'driver=ODBC Driver 17 for SQL Server;server=.\SQLExpress;database=thaivbBiz;trusted_connection=yes;charset=UTF8'
sql = """
    UPDATE Product 
    SET ProductName = 'กางเกงขายาว' 
    WHERE ProductID = '1002'
"""
with pyodbc.connect(strConn) as Conn:
    data = Conn.execute(sql)

print('แก้ไขข้อมูลสินค้าเรียบร้อยแล้ว')

print('รหัสสินค้า' + '\tชื่อสินค้า' + '\t\tต้นทุน' + '\t\tราคาขาย')
print('-----------------------------------------------------------')
with pyodbc.connect(strConn) as Conn:
    sql = 'SELECT ProductID, ProductName, ProductCost, ProductPrice FROM Product' 
    data = Conn.execute(sql)
    for item in data:
        print(str(item[0]).ljust(10) + '\t' + str(item[1]).ljust(20) 
              + str(item[2]) + '\t' + str(item[3]))

