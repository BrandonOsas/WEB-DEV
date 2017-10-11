#! /usr/local/bin/python3.5
import mysql.connector
""" MySQL database and Python """
conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='')
if conn.is_connected():
   print('Connected to MySQL database')
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM animals")
   rows = cursor.fetchall()
   print('Total Row(s):', cursor.rowcount)
   for row in rows:
       print(row) 
   cursor.close()
conn.close()
 
 
