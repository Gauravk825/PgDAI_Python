# -*- coding: utf-8 -*-
"""
Write a python program to accept user name and password and validate it. username
should contain only alphabets or digits and password length should be 8, starts with
alphabet and should contain at least one special character(#,@) .
accept username and password from user and validate it. if it is valid then display message
welcome to our application. otherwise ask to re-enter.
(allows maximum 3 attempts to accept passwordCreated 


"""
import re

user_name=input("Enter user Name : ")
# pattern for user name 
pattern = re.compile(r"^[a-zA-Z0-9_]+")
match1 = pattern.match(user_name)
if match1 != None:
    cnt=0
    # while is use to set count for wrong atempt
    while True:
        passward = input("Ënter passward : ")
        #pattern for passward
        pattern2=re.compile(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$")
    
        match2=pattern2.search(passward)
        if match2:
            print("Passward is valid. ")
            break
            
        else:
            if cnt<3: 
                print("Enter valid valdid passward : ")
                cnt +=1
            else:
                print("Out from maximum limit ")
        
else:
    print("Enter valid user name")
        
