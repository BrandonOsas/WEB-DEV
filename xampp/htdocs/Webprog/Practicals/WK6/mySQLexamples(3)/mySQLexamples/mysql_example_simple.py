import mysql.connector
from mysql.connector import Error
 
 
""" Connect to MySQL database """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
   print('Connected to MySQL database')
 
conn.close()
 
 
