#! /usr/local/bin/python3.5
import cgi, cgitb

cgitb.enable() 
text = 'lovely bunch of bananas'
template = """
 <!DOCTYPE html>
 <html>
 <head>
 <title>Template Example</title>
 </head>
 <body style='background:#00FF00;'>
 <h1>Here-Doc Example</h1>
 <p>{text}</p>
 </body>
 </html>
"""
print('content-type: text/html \n')
print (template.format(text=text)) 
