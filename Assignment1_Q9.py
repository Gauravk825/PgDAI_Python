year = int(input("Enter year: ")) # input for year

if year%100 == 0: # condition for leap year
    if y%400 == 0:
        print(f"Year {year} is a Leap year")
    else:
        print(f"Year {year} is not a leap year")
elif year%4 ==0:
    print(f"Year {year} is a Leap year")

else:
    print(f"Year {year} is not a Leap year")
     

