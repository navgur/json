import json
dict={"rani":"teena",5:9}


a=open("myfile .json","r")
b=json.load(a)
a.close() 
print(b)

