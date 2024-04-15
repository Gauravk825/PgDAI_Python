import sys
choice = 0
while(choice!=5):
    choice = int(input(''' Which pattern you want?
    1)
        *
        **
        ***
        ****
    2)
        *
        ***
        *****
        ***
        *
    3)
        1010101
        10101
        101
        1
    4)
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5

    5) Exit
    Enter your choice
    '''))
    match choice:
        #Triangle Pattern
        case 1:
            num = int(input("Enter number :"))
            for i in range(num):
                print("* "*i)   
            print()
        #Diamond Pattern (for odd numbers)
        case 2:
            num = int(input("Enter odd number : "))
            for i in range(1,num+1,2): # 1 3 5
                print(" "*((num-i)//2) + "*"*(i) )
            for j in range(num-2,0,-2): # 3 1
                print(" "*((num-j)//2) + "*"*(j) )
            print()

        #3) Binary pattern
        case 3:
            num = int(input("Enter number : ")) 
            for i in range(1,num+1):
                print(" "*(i-1) + "10"*(num-i) + "1",end="")
            print()

        # 12345 in triangle Pattern
        case 4:
            num = int(input("Enter number : "))
            for i in range(1,num+1):  
                for j in range(1,i+1):
                    print(str(j) + " ",end="")
                    print()
        case 5:
            sys.exit(0)



