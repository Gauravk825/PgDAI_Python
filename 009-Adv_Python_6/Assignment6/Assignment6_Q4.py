sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}

# removing values from dictionary
n1="name"
n2='salary'
if n1 in sampleDict :
    sampleDict.pop(n1,-1)
if n2 in sampleDict:
    sampleDict.pop(n2,-1)
        
print(sampleDict)