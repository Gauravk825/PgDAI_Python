import re
mno=input("Enter mobile number")
a=re.search("\d{10}",mno)
if a==None:
    print("Invalid Number")
else:
    print("Valid Number")
