__author__ = 'akshaysingh'

import requests

f = open('filename', 'r')
x = f.read().splitlines()
a = 1

for i in x:
    try:
        r = requests.get(i)
        foundClick = dict(r.headers).get('X-Frame-Options')
   
        #print(foundClick)

        if(str(foundClick) == 'None'):
            print(a,"FOUND CLICKJACK ", i)
            a = a + 1
        else:
            print("Not Vulnerable ", i, foundClick, "------------------")
    except:
        print("ERROR ", i, r.status_code, "------------------")









