__author__ = 'akshaysingh'

import requests

f = open('filename', 'r') #Put your filename that has all the website links.
x = f.read().splitlines()
a = 1

for i in x:
    try:
        r = requests.get(i)
        foundClick = dict(r.headers).get('X-Frame-Options') #Checks X-Frame-Options
   
        #print(foundClick)

        if(str(foundClick) == 'None'): #If X-Frame-Option is set to none
            print(a,"FOUND CLICKJACK ", i)
            a = a + 1
        else:
            print("Not Vulnerable ", i, foundClick, "------------------")
    except:
        print("ERROR ", i, r.status_code, "------------------")









