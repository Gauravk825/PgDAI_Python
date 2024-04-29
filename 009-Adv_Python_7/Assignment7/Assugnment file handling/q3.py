import os
lstItems=[]
lstItemsPrice=[]
with open("productdata.txt") as fh1:
    for i in fh1:
            lstItems.append(i.rstrip("\n").split(":")[3])
            lstItemsPrice.append(i.rstrip("\n").split(":")[4])

setitems=set(lstItems)
l3=[]
for i in range(0,len(lstItems)):
    l3.append((lstItems[i],lstItemsPrice[i]))
print(l3)

for i in setitems:
    total=0
    for a,b in l3:
        if a==i:
            total=total+int(b)
    print(i,total)
    total=0
