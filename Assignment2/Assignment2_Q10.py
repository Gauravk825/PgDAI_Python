import math        

value=int(input("Input the value of x ")) # value of x
noterm=int(input(" Enter Number of terms "))

sum1=0
for i in range(1,noterm+1):
    sum1=sum1+pow(value,2*i-1)*pow(-1,i+1)
print(f"sum of the seris is {sum1}")
    
