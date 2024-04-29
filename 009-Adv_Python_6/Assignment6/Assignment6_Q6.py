sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}

#getting value of city 
value = sampleDict.pop('city')

# store new key value pair
sampleDict["location"] = value
print(sampleDict)
