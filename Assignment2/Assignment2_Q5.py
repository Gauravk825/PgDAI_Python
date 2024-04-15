num  = int(input("Enter number: ")) # input for number
count = 0 # intializing the count for number of digit
sum_of_digit = 0 
while(num>0):
    rem = num%10 
    num = num//10
    sum_of_digit =  sum_of_digit + rem # sum of digit
    count += 1 # count number of digit

print(f"Number of digit is {count}")
print(f"Sum of number of digit number is {sum_of_digit}")
