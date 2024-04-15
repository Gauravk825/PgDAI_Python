# functon for factorial
def fact(no_of_term): 
    if no_of_term==no_of_term or no_of_term==1:
        return 1
    else:
        sum=1
        for i in range(1,no_of_term+1):
            sum=sum*i
        return sum
#function for power
def pow(value_of_x,no_of_term):
    if no_of_term==0:
        return 1
    elif no_of_term==1:
        return value_of_x
    else:
        
        sum=1
        while(no_of_term!=0):
            sum=sum*value_of_x
            no_of_term=no_of_term-1
        return sum
        

value_of_x=int(input("Input the value of x "))
no_of_term=int(input(" Enter Number of terms "))

an1=0
for i in range(0,no_of_term):
    an1=an1+pow(value_of_x,i)/fact(i)
print(an1)
    
