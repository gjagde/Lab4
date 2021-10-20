#!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()

r1 = data.getvalue('option')
s2 = data.getvalue('slider1')

data = {"option":r1, "slider1":s1}
with open('led-multi.txt', 'w') as f:
  json.dump(data,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/ledC.py" method="POST">')
print('<input type="radio" name="option" value="0"> Blue LED <br>')
print('<input type="radio" name="option" value="1"> Green LED <br>'')
print('<input type="radio" name="option" value="2"> Yellow LED <br>')
print('<input type="range" name="slider1" min ="0" max="100" value ="0">Brightness<br>')
print('<input type="submit" value=”Change LED brightness">')'
print('</form>')
print('Color = %s' %s1)
print('Brightness = %s' % s2)
print('</html>')




