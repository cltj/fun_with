import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()

server = os.getenv("SQL_SERVER_NAME") # SQL_SERVER_NAME
database = os.getenv("SQL_DATABASE") # SQL_DATABASE
username = os.getenv("SQL_USER_NAME") # SQL_USER_NAME
password = os.getenv("SQL_PASSWORD") # SQL_PASSWORD
driver= '{ODBC Driver 18 for SQL Server}'

def sql_operation(table, operation, values):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            if operation == 'createTable':
                cursor.execute(
                    '''DROP TABLE IF EXISTS dbo.''' + table + '''
                    CREATE TABLE dbo.''' + table + '''([Person ID] int, [Person Name] nvarchar(20), Stream nvarchar(20))'''
                    )
            elif operation == 'insert':
                cursor.execute("INSERT INTO dbo." + table + "([Person ID], [Person Name]) VALUES(" + values + ")")
            elif operation == 'select':
                cursor.execute("SELECT " + values + " FROM " + table)
                row = cursor.fetchall()
                for item in row:
                    print(item)
            elif operation == 'update':
                cursor.execute("UPDATE [dbo].[" + table + "] SET Stream = " + values + " WHERE [Person ID] = 1414")
            elif operation == 'delete':
                cursor.execute("DELETE FROM dbo.[" + table + "] WHERE [Person ID] = " + values + "")
            else:
                print("No operation matched")


def main():
    #sql_operation(table='Persons', operation='createTable', values='')
    #sql_operation(table='Persons', operation='insert', values="1414,'Hans'")
    #sql_operation(table='Persons', operation='select', values="*")
    #sql_operation(table='Persons', operation='update', values="'Electrical'")
    sql_operation(table='Persons', operation='delete', values="1010")

if __name__ == "__main__":
    main()