import pyodbc

strConn = 'driver=ODBC Driver 17 for SQL Server;server=.\SQLExpress;database=thaivbBiz;trusted_connection=yes;charset=UTF8'
sql = """
    INSERT INTO Product(ProductID, ProductName, ProductCost, ProductPrice) 
    VALUES('1009', 'แหวน', 100, 150) 
"""
sql.encode(encoding='UTF-8',errors='strict')

with pyodbc.connect(strConn) as Conn:
    Conn.execute(sql)
print('เพิ่มข้อมูลสินค้าเรียบร้อยแล้ว')

print('รหัสสินค้า' + '\tชื่อสินค้า' + '\t\tต้นทุน' + '\t\tราคาขาย')
print('-----------------------------------------------------------')
with pyodbc.connect(strConn) as Conn:
    sql = 'SELECT ProductID, ProductName, ProductCost, ProductPrice FROM Product' 
    data = Conn.execute(sql)
    for item in data:
        print(str(item[0]).ljust(10) + '\t' + str(item[1]).ljust(20) 
              + str(item[2]) + '\t' + str(item[3]))

