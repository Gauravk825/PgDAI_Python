units = int(input("Enter number of units: ")) # input for units
charge = 0 # intialize charge 
if units <= 100: # for unit less tha 100f
    print("No charge")
elif units > 100 and units <=200:
    charge += 5*(units-100) # charge between 100 to 200
    print(f"Charge for {units} units : {charge}")
elif units > 200:
    units = units%200
    charge += units*10 # charge above 200 
    charge +=5*100 # charge beween 100 to 200
    print(f"Charge for {units} units : {charge}")
    

    
