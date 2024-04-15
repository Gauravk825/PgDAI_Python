num1 = int(input("Enter first number: ")) # input for fisrt number
num2 = int(input("Enter second number: ")) # input for second number

# 4 16 --> HCF is 4
# 20 16 --> HCF is 4

hcf = 0
# chek for mnimum value
if num1<num2:
    num = num1
else:
    num = num2

# claculat hcf
for i in range(1,n+1):
    if num1%i == 0 and num2%i == 0:
        hcf = i
print(f"HCf or GCD of {num1} and {num2} : {hcf}")
    
    
