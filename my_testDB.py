import pyodbc
import pandas as pd

connect = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=103.24.99.76;'
                         'DATABASE=Portal_data;'
                         'UID=testUser;'
                         'PWD=Abcd.1234;')

cursor = connect.cursor()

sql = """SELECT * FROM alfa_sales_and_stock"""
df = pd.read_sql(sql, connect)
# print('DataFrame:\n', df)

csv_data = df.to_csv('Saved_data.csv', index=False, sep='|', encoding='utf-16')


