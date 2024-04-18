# function for factorial
def factorial(num):
    if num==1: # terminated condition
        return 1
    else:
        return num*factorial(num-1)

def main():
    # Print factorial of number from 1 to 20.
    for i in range(1,20+1):
        print(f"{i} {factorial(i)}")
main()
    



