import re
s=input("Enter Sentences")
lst=s.split(".")
lst1=[]
lst2=[]
dict={}
for s in lst:
    a=re.search("[mid]$",s)
    b=re.search("[mM]$",s)
    if a!=None or b!=None :
        lst1.append(s)
    else:
        lst2.append(s)
dict.setdefault("found",lst1)
dict.setdefault("not found",lst2)
print(dict)
