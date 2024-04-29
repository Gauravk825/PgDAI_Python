# Disple all values
sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}

# keys = sampleDict.keys()
# for k in keys:
#     if sampleDict[k]==200:
#         print(sampleDict.get(k))


d3 = sampleDict.items()
for inx,data in enumerate(d3):
    if data[1]==200:
        print(data)