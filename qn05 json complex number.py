import json
# def complexnumber(object):
#     if "complex" in object:
#         return object 

# complex_object=json.loads('{"complex":true,"real":4,"img":5}')
# simple_object=json.loads('{"real":4,"img":3}')
# print("compex_object:",complex_object)
# print("without complex object:",simple_object)





a='{"rani":4,"teena":5+4j}'
d=json.loads(a)
print(d)