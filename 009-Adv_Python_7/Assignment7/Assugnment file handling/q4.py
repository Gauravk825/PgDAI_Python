import os
cat=input("Enter Category")
cat=cat+":"
with open("productdata.txt") as fh1:
    for i in fh1:
        if cat in i:
            print(i)