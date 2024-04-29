from functools import reduce
sampleDict = {
'Physics': 82,
'Math': 65,
'history': 75
}
# creating of values 
values = sampleDict.values()
# for find out larges tvalue in list
largest = reduce(lambda x, y : x if x > y else y, values)
# for print the kay of largest value
for k in sampleDict :
    if sampleDict[k] == largest:
        print(k, sampleDict[k])