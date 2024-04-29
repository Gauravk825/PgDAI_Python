
from bankclass import *

acclst=[Savings("Gaurav", 1024, 40000.00, 20.00),
        Current("Mitali", 3468, 30000.00, 6),
        Current("Utsav",6754 , 80000.00, 15)] 

# to create new account
def createnewaccount(ch) :
    name = input("Enter name :")
    pin = int(input("Enter pin : "))
    
    if ch == 1 :
        bal = float(input("Enter starting balance (more than 5000.00) : "))
        ecs = float(input("Enter ECS amount : "))
        a = Savings(name, pin, bal, ecs)
    elif ch == 2 :
        bal = float(input("Enter starting balance (more than 1000.00) : "))
        a = Current(name, pin, bal, 0)
        
    else:
        bal = float(input("Enter starting balance (more than 6000.00) : "))
        comm =  0.05 * bal
        a = Demat(name, pin, bal, comm)
        

def findByAcc(accno, name):
    for ind,ob in enumerate(acclst):
        if ob.get_accno() == accno and ob.get_name() == name:
            return ind,ob
    return -1,None


# to change pin 
def changepin() :
    accno = input("Enter account : ")
    name = input("Enter name :")
    pos, a=findByAcc(accno, name)
    if pos != -1 :
        npin = int(input("Enter new pin : "))
        a.set_pin(npin)
        print("New pin updated")
    #print(a.get_pin())
    else :
        print("User Not Found\nEnter valid account number and name")
        
#for closing account
def closeaccount() :
    accno = input("Enter account : ")
    name = input("Enter name :")
    pos, a=findByAcc(accno, name)
    if a != None :
        print(a)
        ans = input("Do you want to delete the account?(y/n)")
        if ans == "y" :
            acclst.pop(pos)
            return 1
        else :
           return 2
    else :
        return 3

#getting account details by pin    
def findByPin(naccno, npin):
    for ind,ob in enumerate(acclst):
        #print(ob.get_accno(), ob.get_pin())
        if ob.get_accno() == naccno and ob.get_pin() == npin:
            return ind,ob
    return -1,None
  
#checking balance
def checkbalance() :
    accno = input("Enter account : ")
    pin = int(input("Enter pin :"))
    pos, a=findByPin(accno, pin)
    if a != None :
        #print(a.get_name() , a.get_balance())
        return a.get_name() , a.get_balance()
   
    else :
        return None, -1

# Depositing money 
def deposit() :
    accno = input("Enter account : ")
    pin = int(input("Enter pin :"))
    pos, a=findByPin(accno, pin)
    if a != None :
        #print(a.get_name() , a.get_balance())
        bal = a.get_balance()
        amt = float(input("Enter amount : "))
        bal += amt
        a.set_balance(bal)
        return a.get_name() , a.get_balance()
    else :
        return None, -1
    
    
# Withdrawing money
def withdraw_mon(ch) :
    accno = input("Enter account : ")
    pin = int(input("Enter pin :"))
    namt = float(input("Enter amount :"))
    pos, a=findByPin(accno, pin)
    if a != None :
        if ch == 1 :
            ans = a.withdrawl(namt)
            if ans == True :
                return a.get_balance()
            else :
               return -1
    
        elif ch == 2 :
            a.withdrawl(namt)
            if ans == True :
                return a.get_balance()
            else :
               return -1
        elif ch == 3 :
            a.withdrawl(namt)
            if ans == True :
                return a.get_balance()
            else :
               return -1
    else :
        return 2
         
        
    




# menu driven 
choice=0
while choice!=7:
    choice=int(input("1. Create new account \n2. Withdraw money \n3. Deposit money \n4. Change pin \n5. Check balance \n6. Close Account \n7. Exit \nEnter choice :"))
    
    match choice:
        case 1:
            ch=int(input("1. Savings\n2. Current\n3. Demat\n"))
            createnewaccount(ch)
        case 2:
            ch=int(input("1. Savings\n2. Current\n 3. Demat\n"))
            status = withdraw_mon(ch)
            if status == -1 :
                print("You cannot withdraw amount")
            elif status == 2 :
                print("Please enter correct account number and pin")
            else :
                print(status)
                
                
            
        case 3:
            name, balance = deposit()
            if name != None :
                print(f" Name : {name}\n Balance : {balance}")
            else :
                print("Please enter correct account number and pin")
                
        case 4:
            changepin()
        case 5:
           name, balance = checkbalance()
           if balance != -1 :
               print(f" Name : {name}\n Balance : {balance}")
           else :
               print("Please enter correct account number and pin")
               
        case 6:
            status = closeaccount()
            if status==1:
                print("Found and Deleted")
            elif status==2:
                print("Found but not Deleted")
            else:
                print("User Not Found\nEnter valid account number and name")
            
        case 7:
            print("Thank you for visiting....")
        case _ :
            print("Invalid option")



