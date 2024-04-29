#line   = """2.Accept lines from user and display only the lines that start with an number or any 2 alphabets"""
import re

# input string forom user
lst1 = list((x for x in input("Enter cities : ").split('.')))

# for display only the lines that start with an number or any 2 alphabets
for line in lst1: 
    pattern = re.compile(r'\b([a-zA-Z][a-zA-Z])\b | \d\b')
    matches=pattern.search(line)
    if matches!=None:
        print(line)
