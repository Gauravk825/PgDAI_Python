sum_of_even = 0
for i in range(20):
    num = int(input("Enter Number : ")) # input from user 
    if num%2==0:
        sum_of_even += num # Addition of even number
print(f"Sum of Even Numbers :{sum_of_even}")
