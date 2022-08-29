import json

dict1 ={
    'emp1': {
        'name': "Lisa",
        "designation": "programmer",
        'age': "34",
        'salary': "54000"
    },
    'emp2': {
        'name': "Elis",
        'designation': "Trainee",
        'age': "24",
        'salary': "40000"
    },
}

# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()

Out_file =open("myfile .json","w")
a=json.dump(dict1, Out_file,indent=2)
Out_file.close()
print(a)

# f=open("myfile .json","r")  
# a=json.load(f)
# print(a)
# print(type(a))

