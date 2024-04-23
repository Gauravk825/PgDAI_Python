lst = []
# continue the loop until user want enter the number
while True:
    num = int(input("Enter number : "))
    last_digit = num % 10
    # to check last dgit is greater than lenght of list
    if last_digit>len(lst):
        # for append list into list
        for i in range (0,(last_digit-len(lst))+1) :
            lst.append(list())
            print(lst)
    lst[last_digit].append(num)
    print(lst)
    
    # loop terminatar
    ans = input("Do you want to continue y/n : ")
    if ans =="n":
        break
        