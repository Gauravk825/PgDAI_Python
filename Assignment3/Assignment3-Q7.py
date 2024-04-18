#  function for sum 1 to n
def sum1(num):
    if num<=1: # terminated condition
        return 1
    else:
        return num+sum1(num-1) # recursion

def main():
    # Print sum of number.
    num = int(input("Enter Number :"))
    print(f"Sum of 1 to {num} is {sum1(num)}")
main()
    
