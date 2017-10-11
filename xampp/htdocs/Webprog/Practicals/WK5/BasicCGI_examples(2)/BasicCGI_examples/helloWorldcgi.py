#! /usr/local/bin/python3.5

import os

print "Content-type: text/html\r\n\r\n";
print "<font size=+1>Environment</font></br>";
for param in os.environ.keys():
  print ("<b>", param, "</b>: ", os.environ[param], "</br>")

