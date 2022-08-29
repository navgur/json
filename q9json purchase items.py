import json

a={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}

s=open("myfie","w")
g=json.dump(a,s,indent=2)
s.close()
f=open("myfie.json","r")
h=json.load(f)
f.close()
print(h)
b=(input("enter the item names"))
c=int(input("how many items do you want?"))
for  i in h:
    for j in h[i]:
        if j==b and int(h[i][j])>c:
            e=int(h[i][j])-c
            h[i][j]=str(e)
        elif j!=b:
            print("ok")
            break
ite=input("enter items")
q=int(input("enter the num="))
h[i].update({ite:q})
print(h)

