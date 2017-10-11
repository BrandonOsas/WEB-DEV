import mysql.connector
 
""" MySQL database and Python """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
  print('Connected to MySQL database')
  cursor = conn.cursor()


  cursor.callproc('find_all')
 
  # print out the result
  for result in cursor.stored_results():
      print(result.fetchall())  
 
  cursor.close()

conn.close()
 
 
