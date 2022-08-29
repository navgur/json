import json
Text_txt=  "Name Abhishek Designatio CEO of navgurukul Gender male Age 29 "
a=Text_txt.split()
key=[]
value=[]
g={}
for i in range (len(a)):
    if i%2==0:
        k=a[i]
    v=a[i]
    g.update({k:v})
r=open("rfile.json","w")
s=json.dumps(g)
print(s)
    

