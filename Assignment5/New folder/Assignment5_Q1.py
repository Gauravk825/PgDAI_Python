# for displsy even positin of atring
def evenposition(str_input):
    for i in range(1,len(str_input), 2):
##        if i%2==0:
        print(f"{str_input[i]} ", end= " ")
    print()
# for display odd position of string   
def oddPosition(str_input):
    for i in range(len(str_input)):
        if i%2!=0:
            print(f"{str_input[i]} ", end= " ")
    print()
# for display the lenght of string
def lengthofstring(str_input):
    print(f"Length of string is : {len(str_input)}")
    
# for adding a at end of the string length times
def add_a_at_end(str_input):
    print(str_input + 'a'*len(str_input))

choice=0
while choice!=5:
    choice =int(input(''' 1) Display charecter from even postion
    2) Diplay charecter from odd position
    3) Display length of string
    4) Add length of a string
    5) Exit
    Enter choice: '''))
    match choice:
        
        case 1:
            str_input = input("Enter string")
            evenposition(str_input)
        case 2:
            str_input = input("Enter string")
            oddPosition(str_input)
        case 3:
            str_input = input("Enter string")
            lengthofstring(str_input)
        case 4:
            str_input = input("Enter string")
            add_a_at_end(str_input)
        case 5:
            print("Thankyou for visiting....")
        case _:
            print("Wrong choice")
