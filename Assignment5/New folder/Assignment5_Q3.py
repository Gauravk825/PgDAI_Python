#to add  last postion
def addlast(last, lst) :
    lst.append(last)
    print(lst)

#to add given postion
def addatgivenpos(data, index, lst) :
    lst[index] = data
    print(lst)

#to delete data by value
def deletebyvalue(value, lst) :
    if lst.count(value) == 0 :
        return 0
    else :
        while value in lst :
            lst.remove(value)
        return 1

#to delete from last position
def deletefromlast(lst) :
    lst.pop()
    print(lst)
    print("Last element deleted")

#to delete by position
def deletebypos(pos, lst) :
    value = lst.pop(pos)
    return value

#to sort in ascending order (sorted)
def ascendingsorted(lst) :
    sortlst = []
    sortlst = sorted(lst)
    print(sortlst)

#to sort in ascending order
def ascending(lst) :
    lst.sort()
    print(lst)


#to sort in descending order
def descending(lst) :
    lst.sort(reverse = True)
    print(lst)

#to reverse list
def reverselist(lst) :
    lst.reverse()
    print(lst)
    
#to reverse list (reversed)
def list_reversed(lst) :
    revlst= list(reversed(lst))
    print(revlst)
    
#to display data
def displaydata(lst) :
    print(lst)

#to display numbered data
def numbereddata(lst) :
    print(list(enumerate(lst)))

lst = [1, 2, 3, 6, 7, 8, 2,7 ,7 , 9]
choice=0
while choice!=9:
    choice = int(input('''
    1) Accept Data
    2) Delete data by value
    3) Delete data by position
    4) sort
    5) Reverse
    6) Print in sord order without changing original list
    7) Print reverse order without changing original list
    8) Display data
    9) Exit
    Enter choice : '''))

    match choice:
        case 1:
            ans = input('''a)Add last postion \nb)Add given posion \nEnter choice : ''')
            if ans=="a":
                last = input("Enter data to add at last position: ")
                addlast(last, lst)
            else :
                data = input("Enter data to add: ")
                index = int
                (input("Enter position: "))
                addatgivenpos(data, index, lst)
        case 2:
            ans = int(input("Enter value to delete : "))
            status = deletebyvalue(ans, lst)
            if status == 1 :
                print(f" {ans} deleted successfully from list")
            else :
                print("Not Found")
        case 3 :
            ans = input('''a)delete last element \nb)delete from particular position \nEnter choice : ''')
            if ans=="a":
                deletefromlast(lst)
            else :
                ans = int(input("Enter position to delete : "))
                status = deletebypos(ans, lst)
                print(f" {status} deleted from list")
        case 4 :
            ans = input('''a)Sort in ascending order \nb)Sort in descending order \nEnter choice : ''')
            if ans=="a":
                ascending(lst)
            else :
                descending(lst)
        case 5 :
            reverselist(lst)
        case 6 :
            ascendingsorted(lst)
        case 7 :
            list_reversed(lst)
        case 8:
            ans = input('''a)Normal \nb)Numbered \nEnter choice : ''')
            if ans=="a":
                displaydata(lst)
            else :
                numbereddata(lst)
        case 9 :
            print("Thank you for visiting...")
        case _ :
            print("Invalid option")

            
            
            
            


                

