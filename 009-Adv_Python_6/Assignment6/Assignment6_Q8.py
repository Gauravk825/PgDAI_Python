sampleDict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}

ename = input("Enter name : ")
sal = int(input("Enter salary : "))

for emp in sampleDict:
    if ename in sampleDict[emp]['name']:
        sampleDict[emp]["salary"] =sal
        print(sampleDict)

