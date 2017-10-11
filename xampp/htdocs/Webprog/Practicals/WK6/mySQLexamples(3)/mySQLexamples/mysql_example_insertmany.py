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
  
  args = [(14, 'babytiger'),
             (15, 'shark'),
             (16, 'wolf')]

  cursor.executemany(query,args)  
  conn.commit()    
  cursor.close()

conn.close()
 
 
