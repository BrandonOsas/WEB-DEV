#! /usr/local/bin/python3

print ('Content-type:text/html \n')
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h1>Hello Word! This is my first CGI program</h1>')
print ('</body>')
print ('</html>')


file = open("newfile.txt", "w")
file.write("hello world in the new file\n")
file.write("and another line\n")
file.close()

file = open("newfile.txt", "r")
for line in file:
    print (line,)
file.close()

