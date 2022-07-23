import pyodbc
import csv

connect = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=SNIKERZZ\SQLEXPRESS;'
                         'DATABASE=testDB;')

cursor = connect.cursor()


with open('Saved_data.csv','r', encoding='utf-16') as file:
    dr = csv.DictReader(file, delimiter='|')
    to_db = [(i['medicament'], i['consumption_value'], i['all_value']) for i in dr]

sql_1 = """INSERT INTO alfa_sales_and_stock(medicament,consumption_value,all_value) VALUES (?, ?, ?)"""
cursor.executemany(sql_1, to_db)
connect.commit()
connect.close()

# for row in cursor.tables():
#     if row[3] == 'TABLE':
#         print(row[2])


# cursor.execute('''select * from alfa_sales_and_stock''')
# rows = cursor.fetchmany()
# print(rows)