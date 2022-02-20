import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

server = 'cltj.database.windows.net'
database = 'test'
username = os.getenv("SQL_USER_NAME") # SQL_USER_NAME
password = os.getenv("SQL_PASSWORD") # SQL_PASSWORD
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT @@Version")
        row = cursor.fetchall()
        print(row)