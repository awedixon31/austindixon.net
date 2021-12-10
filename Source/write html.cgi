
f = open('/helloworld.html','w')

message = """<html>
<head></head>
<body><h1>Hello World!</h1></body>
</html>"""

f.write(message)
f.close()

filename = 'file:////helloworld.html/' + 'helloworld.html'
webbrowser.open_new_tab(filename)