import requests
import json
d=requests.get("https://www.merakilearn.org/course-content/miscellaneous/3/0")
c=d.json()
f=open("json.txt","w")
s=json.dump(c,f,indent=2)

z=open("json.txt","r")
x=json.load(z)
c=json.loads(x)

