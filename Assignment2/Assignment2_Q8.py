term = int(input("Enter nmber of terms")) # number of term from user 
add = 0 
for i in range(1,term+1):
        print("9"*i,end =" ") # arrenge in series order
        value = int("9"*i)
        add += value
        

print() # for print order
print(f"Sum of series is : {add}")
