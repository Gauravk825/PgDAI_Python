choice=1
lst=[]
while choice!=0:
    choice=int(input("Enter 1 for next entru 0 for exit"))
    match choice:
        case 1:
            lst1=input("Enter data ").split(",")
            lst.append(lst1)
            pass
        case 0:
            print("Thanks for using")
            pass
for i in lst:
    if int(i[2])==2018:
        print(f"{i[1]}---2018")
for i in lst:
    if i[5]=="pune":
        print(i[1],"--pune")