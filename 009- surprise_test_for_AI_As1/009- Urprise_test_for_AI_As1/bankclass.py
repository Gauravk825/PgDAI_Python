from abc import ABC,abstractmethod

class Account(ABC):
    
    # use for auto genreted account number
    cnt = 101
    @staticmethod
    def __generatecode(actype):
        accno = actype + str(Account.cnt)
        Account.cnt = Account.cnt+1
        return accno
    
    def __init__(self, name = "", pin = 0 ,balance = 0.0,  actype = ""):
        self.__accno = Account.__generatecode(actype)
        self.__name = name
        self.__pin = pin
        self._balance = balance

    def get_accno(self):
        return self.__accno 

    def set_name(self, nm):
        self.__name = nm  
    
    def get_name(self) :
        return self.__name
    
    def set_pin(self, pinno) :
        self.__pin = pinno

    def get_pin(self):
        return self.__pin
 
    def set_balance(self, bal) :
        self._balance = bal  
        
    def get_balance(self):
        return self._balance
    
    #abstract method
    @abstractmethod 
    def withdrawl(self):
        pass
    
    def __str__(self) :
        return f"Account No : {self.__accno} \nName : {self.__name} \nBalance : {self._balance}"
    
    
    

# class for saving account           
class Savings(Account) :
    
    # static variavbble 
    intrest_rate_s = 0.4
    minbals = 5000.00
    
    def __init__(self, name = "", pin = 0 ,balance = 0.0, ecs = 0.0, actype = "S") :
        super().__init__( name, pin, balance, actype)
        self.__ecs = ecs
        
    def set_ecs(self, ecs) :
        self.__ecs = ecs
        
    def get_ecs(self):
        return self.__ecs
    
    def get_minbal(self):
        return Savings.min_bal_s
    
    #refined abstract method
    def withdrawl(self, amt_to_withdrael):
       balance_in_acc = self._balance
       min_bal = Savings.min_saving_bal
       if (balance_in_acc - amt_to_withdrael) > min_bal:
           self.set_balance(balance_in_acc-amt_to_withdrael)
           return True
       else :
           return False
       
      
    
    def __str__(self) :
        return super().__str__()+ f" \nECS : {self.__ecs}"
    
    
        
        
          
class Current(Account) :
    
    intrest_rate_s = 0.5
    min_bal_c = 1000.00
    
    def __init__(self, name = "", pin = 0 ,balance = 0.0, transaction = 0, actype ="C" ) :
        super().__init__(name, pin, balance, actype)
        self.__transaction = transaction
        
    def set_transaction(self, trans) :
        self.__transaction = trans
        
    def get_transcation(self):
        return self.__transaction
    
    def __str__(self) :
        return super().__str__()+ f" \nNo. of Transaction : {self.__transaction}"
    
    def withdrawl(self, amt):
        a = self._balance
        
        if a - amt > Current.min_bal_c:
            self.set_balance(a-amt)
            return True
        else :
            return False
        
        
        
class Demat(Account) :
    
    intrest_rate_d = 0.6
    min_bal_s = 6000.00
    
    def __init__(self , name = "", pin = 0 ,balance = 0.0, com = 0.0, actype ="D") :
        super().__init__(name, pin, balance, actype)
        self.__com = com
        
    def set_com(self, commision) :
        self.__com = commision
        
    def get_com(self):
        return self.__com

    def __str__(self) :
        return super().__str__()+ f" \nCommission : {self.__com}"
    
    def withdrawl(self, amt):
        a = self._balance
        
        if a - amt > Demat.min_bal_d:
            self.set_balance(a-amt)
            return True
        else :
            return False
        

        
if __name__=="__main__": 
    ob = Savings("Gaurav", 1024, 4000.00, 20.00)
    print(ob)   
    ob1 = Current("Mitali", 3468, 3000.00, 6)
    print(ob1) 
    ob3 = Demat("Parth", 9076, 67900.00, 0.10)
    print(ob3) 
     
