#! /usr/local/bin/python3.5
import dbfunc, mysql.connector, cgi, cgitb
cgitb.enable()
table  = "animals"
spotted = "spotted"
conn = dbfunc.getConnection()
name = ''
cursor = ''

print ('content-type: text/html \n')
print ('<h1>Animal Selected</h1> <br />')

def selectTable(sqlstat, more): 
  global name
  statement = sqlstat
  cursor.execute(statement, more)
  row = cursor.fetchone()
  name = row[0]
  print ("Animal selected: ", name, "<br />")

def insertTable(sqlstat, more):
  statement = sqlstat
  cursor.execute(statement, more)
  print('<br> Record: ', more, ' inserted')

form = cgi.FieldStorage() 
sql_statement1 = "SELECT name FROM " + table + " WHERE id = %s"
sql_statement2 = "INSERT INTO spotted (animal, count) VALUES (%s, %s)"
keys = list(form.keys())
print ('Length of keys is: ', len(keys))

if conn.is_connected():   
    cursor = conn.cursor()

for animal_id in keys:
  if animal_id is not None:
    amount = form.getvalue(animal_id)
    print ('<br> For ID: ',animal_id, ' I saw amount of ', amount, '<br>')
    args1 = (animal_id,)
    selectTable(sql_statement1, args1)
    args2 = (name, amount)
    insertTable(sql_statement2, args2)

conn.commit()
cursor.close()
conn.close()