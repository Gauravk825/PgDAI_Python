#get only the part of the email before the "@" sign excluding the "@" sign.
s="gauravkumarsuingh825@google.com"
import re

# pattern for find part before @
lst=re.finditer(r"^[a-zA-Z0-9_]*",s,re.I)
# if find the pattern then 
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
else:
    print("not found")
    