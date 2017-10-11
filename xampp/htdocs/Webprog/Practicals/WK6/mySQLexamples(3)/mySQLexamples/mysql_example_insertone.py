import mysql.connector
 
""" MySQL database and Python """

conn = mysql.connector.connect(host='localhost',
                              database='webprog',
                              user='root',
                              password='secret')
if conn.is_connected():
  print('Connected to MySQL database')
  cursor = conn.cursor()
  query = "INSERT INTO animals (id,name) " \
            "VALUES(%s,%s)"
  
  (id, name) = (13, "Cougar")
  args = (id, name)

  cursor.execute(query,args)  
  conn.commit()    
  cursor.close()

conn.close()
 
 
