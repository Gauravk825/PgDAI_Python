from Assignment8_Q3 import *

frndlst = [Friends("Rahul", "Dravid", ["Cricket", "Sports", "Movies"], "9876543289", "12-05-2024", "Mumbai"),
           Friends("Gaurav", "Kumar", ["Music", "Sleeping", "Movies"], "9876590876", "12-09-2000", "Haryana"),
           Friends("Mitali", "Giri", ["Reading", "Drawing", "Movies"], "4527789076", "11-10-2004", "Pune")]

# to display all friends
def displayall():
    for line in frndlst :
        print(line)

#to find friend by id        
def findById(fid):
    for ind,ob in enumerate(frndlst):
        if ob.getid() == fid:
            return ind,ob
    return -1,None

# for find by hobby
def findbyhobby(ho) :
    lst2 = []
    for ind,ob in enumerate(frndlst):
        lst = ob.gethobbies()
        if ho in lst:
            lst2.append(ob)
    if lst2 != None :
        #print(lst2)
        return lst2
    else : 
        return None
# find by name         
def findbyname(name) :
    lst2 = []
    for ind,ob in enumerate(frndlst):
        lst = ob.getname()
        print(lst)
        if name == str(lst):
            return ob
    else : 
        return -1


choice = 0
while choice!= 5 :
    choice = int(input("""\n1. Display All Friend\n2. Search by id\n3. Search by name\n4. Display all friend with a particular hobby\n5. Exit\nEnter choice : """))
    
    match choice :
        case 1 :
            displayall()
        case 2 :
            fid=input("Enter id : ")
            pos,frnd = findById(fid)
            if frnd!=None:
                print(frnd)
            else:
                print("Not found====>",fid)
        case 3 :
           name = input("Enter name for search : ")
           fname = findbyname(name)
           #print(findbyname(name))
           # check eturn value is none or not
           if fname != None : 
               print(fname)
           else :
                print("There is no friend with such hobbies")
        case 4 :
            ho = input("Enter hobby : ")
            fhob = [] # list for store return value from function
            fhob = findbyhobby(ho)
            if fhob != None :
                for hob in fhob :
                    print(hob)
            else :
                print("There is no friend with such hobbies")
        case 5 :
            print("Thank you for visitng")
        case _ :
            print("Invalid option")