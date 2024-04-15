sum_of_num=0
product_of_num=1
count=0
aveg=0
while(1): # for continue asking for number
    value = input("Enter number, if you want to quit then enter 'q' : ")
    if value=='q':
        break
    else:
        sum_of_num = sum_of_num + int(value)
        product_of_num = product_of_num*int(value) 
        count += 1
        

average = sum_of_num/count
print("Average of numbers :", average)
print("Product of numbers :", product_of_num)
