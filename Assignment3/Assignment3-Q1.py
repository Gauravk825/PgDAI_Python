# accepts the number of day in month 29,28,30,31
#when month start
while True:
    numdays= int(input("Enter number of days in month: "))
    if numdays >28 and numdays<=31:
        break
startday = int(input("Enter day of month (0 - Monday, 1 - Tuesday): "))

print("\tMon\tTue\tWed\tThu\tFri\tSat\tSun")
count = startday
#it will print spaces before 1, useful only for line 1
print("\t"*startday, end="")
for i in range(1,numdays+1):
    print("\t"+str(i), end="")
    count += 1
    #to bring the cursor on the nexrt line
    if count == 7:
        print()
        count =0
