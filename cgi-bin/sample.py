import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
for key in form:
    value = form[key].value
    print('<p>%s: %s</p>' % (key, value))


