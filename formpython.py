#!/usr/local/bin/python3
import cgi, cgitb
cgitb.enable ()
print ("Content-type: text/html\n")

form = cgi.FieldStorage()

textfield = form.getvalue('textfieldname')
textarea = form.getvalue('textareaname')


print ("box2={}, box1= {} ".format(textarea,textfield))
