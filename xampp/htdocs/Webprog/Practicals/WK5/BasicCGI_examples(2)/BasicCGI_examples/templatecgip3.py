#! /usr/local/bin/python3.5

# a simple template
template = "<html><body><h1>Hello {tech}. This is {prog}!</h1></body></html>"

print ('Content-type:text/html \n')
print(template.format(tech="Web Programming", prog="Python"))
