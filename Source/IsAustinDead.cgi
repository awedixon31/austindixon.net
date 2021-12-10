#!/usr/bin/python

print 'Content-Type: text/html\n\n'

import urllib,json


url = "http://seeaustinssugar.herokuapp.com/api/v1/entries.json?count=1"
response = urllib.urlopen(url)
string = response.read()
data = json.loads(string[1:-1])


sgv = data['sgv']
direction = data['direction']

a = str(sgv)
b = str(direction)

if b == 'NOT COMPUTABLE':
    b = ('Flat')

    


print('<link rel="shortcut icon" type="image/x-icon" href="favicon.png"  >')


#print ('<link rel="stylesheet" href="fire.scss">')
#print ('<div class="pyro"><div class="before"></div><div class="after"></div></div>')

print ('<link rel="stylesheet" href="IsAustinDeadStyles.css">')
print ('<link rel="stylesheet" href="IsAustinDeadTextStyles.css">')



if sgv >= 180:

    
    #print ('<h3 align="center" class="rainbow">Austin is DEAD. He is HIGH at %s %s</h3>' % (a, b))
    
    print ('<h3 align="center" class="rainbow">Austin is</h3>')
    print ('<h4 align="center" class="rainbow">DEAD </h4>')
    print ('<h5 align="center" class="rainbow">His blood sugar is HIGH at %s </h5>' % (a))
    print('<h6><center><img src="images/stressed.gif"style="width:480px;height:170px;"></center></h6>')

elif sgv <= 80:


    #print ('<h3 align="center" class="rainbow" >Austin is DEAD. He is LOW at %s %s</h3>' % (a, b))
    
    print ('<h3 align="center" class="rainbow">Austin is</h3>')
    print ('<h4 align="center" class="rainbow">DEAD </h4>')
    print ('<h5 align="center" class="rainbow">His blood sugar is LOW at %s </h5>' % (a))
    print('<h6><center><img src="images/low1.gif"style="width:480px;height:170px;"></center></h6>')
        
else:

    print ('<h3 align="center" class="rainbow">Austin is</h3>')
    print ('<h4 align="center" class="rainbow">NOT DEAD </h4>')
    print ('<h5 align="center" class="rainbow">His blood sugar is %s </h5>' % (a))
    print('<h6><center><img src="images/nooice.gif"style="width:480px;height:191px;"></center></h6>')
    print ('<link rel="stylesheet" href="fire.scss">')
    print ('<div class="pyro"><div class="before"></div><div class="after"></div></div>')
    
    
if direction == 'DoubleUp':
    print ('<h3><center><img src="/images/DoubleUp.svg"style="width:240px;height:240px;"></center></h3>')
if direction == 'SingleUp':
    print ('<h3><center><img src="/images/singleup.svg"style="width:240px;height:240px;"></center></h3>')
if direction == 'FortyFiveUp':
    print ('<h3><center><img src="/images/45up.svg"style="width:240px;height:240px;"></center></h3>') 
if direction == 'Flat':
    print ('<h3><center><img src="/images/Flat.svg"style="width:240px;height:240px;"></center></h3>') 
if direction == 'FortyFiveDown':
    print ('<h3><center><img src="/images/45down.svg"style="width:240px;height:240px;"></center></h3>')
if direction == 'SingleDown':
    print ('<h3><center><img src="/images/SingleDown.svg"style="width:240px;height:240px;"></center></h3>')
if direction == 'DoubleDown':
    print ('<h3><center><img src="/images/DoubleDown.svg"style="width:240px;height:240px;"></center></h3>')
if direction == 'None':
    print ('<h3><center><img src="/images/nonesvg.svg"style="width:240px;height:240px;"></center></h3>')

    
