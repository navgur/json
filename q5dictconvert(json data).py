import json
s={
    "4": 5, 
    "6": 7, 
    '1': 3, 
    '2': 4}

a=json.dumps(s)
print(a)
print(type(a))