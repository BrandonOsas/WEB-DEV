#! /Python34/python
import mysql.connector
 
""" Connect to MySQL database """
conn = mysql.connector.connect(host='localhost',
                              database='webair',
                              user='root',
                              password='')
if conn.is_connected():
   #animal_id = Bristol
   #args = (animal_id,)
   print ('Content-type:text/html \n')
   print('<H1> Connected to MySQL database </H1>')
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM timeanddate where leave_airport = 'Bristol'")
   row = cursor.fetchone()
   while row is not None:
       print(row,'</br>')
       row = cursor.fetchone()
   cursor.close()
conn.close()
 
 
