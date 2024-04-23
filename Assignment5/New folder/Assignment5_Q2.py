user_input=input("Enter string : ")
search = input("Ënter string for search")
#first occurnce of string
pos=user_input.find(search)
count = 0
# for search th given string
while pos!=-1:
    print("position :",pos)
    pos=user_input.find(search,pos+1)
    count+=1
