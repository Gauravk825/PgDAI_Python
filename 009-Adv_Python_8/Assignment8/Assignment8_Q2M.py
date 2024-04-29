from Studentclass2 import * 

studlst = [Student(101, "Rahul", 67, 81, 73),
           Student(102, "Mitali", 89, 81, 56),
           Student(103, "Gaurav", 80, 90, 97)]

#to display all students
def displayall() :
    for und in studlst :
        print(und)

#to serach by id 
def searchbyid() :
    id = int(input("Enter id to search : "))
    for ind,ob in enumerate(studlst):
        if ob.getstudid() == id:
            return ind,ob
    return -1,None

#to serach by name
def searchbyname() :
    name = input("Enter name to search : ")
    for ind,ob in enumerate(studlst):
        if ob.getname() == name:
            return ind,ob
    return -1,None

#to galculate gpa of student
def getgpa() :
    id = int(input("Enter id : "))
    for ind,ob in enumerate(studlst):
        if ob.getstudid() == id:
            stgpa = Student.calculategpa(ob.getm1(), ob.getm2(), ob.getm3())
            return stgpa
    return -1

choice = 0
while choice != 5 :
    choice = int(input("1. Display All Students\n2. Search by id\n3. Search by name\n4. calculate GPA of a student\n5. Exit\nEnter choice : "))

    match choice :
        case 1 :
            displayall()
        case 2 :
            indx , obj = searchbyid()
            if indx != -1 :
                print(f"Student Id : {obj.getstudid()}\nName : {obj.getname()}\nMarks 1: {obj.getm1()}\nMarks 2 {obj.getm2()}\nMarks 3: {obj.getm3()}")
            else :
                print("No student by such id")
            
        case 3 :
            indx , obj = searchbyname()
            if indx != -1 :
                print(f"Student Id : {obj.getstudid()}\nName : {obj.getname()}\nMarks 1: {obj.getm1()}\nMarks 2 {obj.getm2()}\nMarks 3: {obj.getm3()}")
            else :
                print("No student by such name")
        case 4 :
            gpa = getgpa()
            if gpa != -1 :
                print(f"The gpa of student is : {gpa}")
            else :
                print("No student by such id")
        case 5 :
            print("Thank you for visiting...")
        case _ :
            print("Invalid Option")