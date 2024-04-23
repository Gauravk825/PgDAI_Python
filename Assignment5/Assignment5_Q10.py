# string for remove spae and det proper punchuation
str1 = "This is very     funny and cool.Indeed!"

# for removing space and add space after (.)
def correct(str1):
    str2 =""
    # for position and string 
    for indx,ch in enumerate(str1) :
        if ch == " " and str1[indx+1]== " ":
            ch.rstrip(" ")
        else :
            str2 = str2 + ch

        if ch == "." and str1[indx+1]!= " ":
            str2 = str2 + " "

    print(str2)
# calling function
correct(str1)
