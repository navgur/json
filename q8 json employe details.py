import json

a=[["neelam","programmer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["abhishek","manager","29","63000"]]
key=["name","designation","age","salary"]
keyy=["emp1","emp2","emp3","emp4"]
d={}
t={}
for i in  range  (len(key)):
    for i in range (len(a)):
        for j in range (len(a[i])):
            d.update({key[i]:a[j][i]})
            t.update({keyy[i]:d})
print(t)
#             d.update({keyy[i]:g})
# print(d)

         
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
    #     "Designation":"Trainee",
    #     "Age":"24",
    #     "salary":"20000" ,
    #     }

 
    # "emp3":
    #    { "name":"anuradha",
    #      "Designation":"HR",
    #      "Age":"25",
    #      "salary":"40000",