import os
import re
lst=[]
lstItems=[]
lstItemsPrice=[]
m=re.compile("^12.*0$")
with open("productdata.txt") as fh1:
    for i in fh1:
        a=m.search(i)
        if a!=None:
            lst.append(i)
with open("myproduct.txt","w") as fh1:
    for i in lst:
        fh1.write(i) 
