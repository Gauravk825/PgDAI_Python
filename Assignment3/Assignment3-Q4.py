comp_str = "abcdefghijklmnopqrstuvwxyz" 
str1 = input("Enter the String : ") # input for string
str2 = str1.lower() #change string into lower string
result=""
# check for alphbets and store in string variable
for ch in str2:
    if ch.isalpha():
        result = result+ch
#Check if all elements are present or not
for ch in comp_str:
    # check if charecter(a-z) is present in result(string)
    if ch in result:
        flag=1
    else:
        flag=0

if flag==1:
    print("String is Pangram")
else:
    print("String is Not Pangram")
