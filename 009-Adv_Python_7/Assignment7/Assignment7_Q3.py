# Write a python program to accept mobile number and validate it. it should contain exactly 10 digits.
import re

# regular expression for accpt mobile number
pattern = re.compile(r"\d{10}\b")

mob_num=""
# for compare the mobile number with regular expression
while True:
    mob_num = input("Enter mobile number : ")
    match = pattern.match(mob_num)
    if match!=None:
        print(mob_num)
        break
        
    else:
        print("Not Valid mobile number")