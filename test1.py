import pyodbc

connect = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=tcp:SNIKERZZ\SQLEXPRESS,49999;'
                         'DATABASE=testDB;'
                         'UID=testuser;'
                         'PWD=password;')

# cursor = connect.cursor()

# for row in cursor.tables():
#     if row[3] == 'TABLE':
#         print(row[2])
