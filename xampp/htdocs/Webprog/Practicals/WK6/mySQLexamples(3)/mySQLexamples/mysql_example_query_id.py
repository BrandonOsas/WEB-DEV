#! /Python34/python
import mysql.connector

animal_id = Bristol
args = (animal_id,)
conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')
if conn.is_connected():
   print('Connected to MySQL database')
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM timeanddate WHERE leave_airport = %s",args)
   row = cursor.fetchone()
   while row is not None:
       print(row)
       row = cursor.fetchone()
   cursor.close()
else:
   print("%s", args)
conn.close()
 
 
