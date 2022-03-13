# Establishing a Connection

from getpass import getpass
from mysql.connector import connect, Error
import os
from dotenv import load_dotenv
load_dotenv()

server = os.getenv("mySQL_SERVER_NAME") # SQL_SERVER_NAME
database = os.getenv("mySQL_DATABASE") # SQL_DATABASE
username = os.getenv("mySQL_USER_NAME") # SQL_USER_NAME
myPassword = os.getenv("mySQL_PASSWORD") # SQL_PASSWORD

try:
    with connect(
        host=server,
        user=username,
        password=myPassword,
    ) as connection:
        print(connection)
except Error as e:
    print(e)