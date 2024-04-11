price = int(input("Enter the price of a bike(in k): ")) # input for price

if price > 100:
    print(f"Tax amount = {price*15/100}") # tax 15%
    print(f"Insurance = {price*20/100}") # insurance 20%
    print(f"Total amount = {price+(price*20/100)+(price*15/100)}")
elif amount > 50 and amount <= 100:
    print(f"Tax amount = {price*10/100}") # tax 10%
    print(f"Insurance amount = {price*8/100}")# insurance 8%
    print(f"Total amount= {price+(price*10/100)+(price*8/100)}") # total amount
else:
    print(f"Tax amount = {price*5/100}") # tax 5%
    print(f"Insurance amount = {price*5/100}") # insurance 5%
    print(f"Total amount = {price+(price*5/100)+(price*5/100)}")# total amount
    
    
