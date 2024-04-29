class Person:
    def __init__(self,id,name,email):
        self.__id=id
        self.__name=name
        self.__email=email
    def __str__(self):
        return f"id:{self.__id}+name:{self.__name}+email{self.__email}"


class Vendors(Person):
    def __init__(self, id, name, email,phoneno,listOfProduct):
        super(self).__init__(id, name, email)
        self.__phoneno=phoneno
        self.__listOfProduct=listOfProduct
    
    def __str__(self):
        return Person.__str__(self)+f"phone no:{self.__phoneno}+list of products:{self.__listOfProduct}+email{self.__email}"


class Customer(Person):
    def __init__(self, id, name, email,creditClass,disc,plan):
        self.__creditClass=creditClass
        self.__disc=disc
        self.__plan=plan
    def __str__(self):
        return Person.__str__(self)+f"creditClass:{self.__creditClass}+disc:{self.__disc}+plan{self.__plan}"


class IndiCustomer(Customer):
    def __init__(self, id, name, email, creditClass, disc, plan,phoneno):
        super(self).__init__(id, name, email, creditClass, disc, plan)
        self.__phneno=phoneno
    def __str__(self):
        return Customer.__str__(self)+f"+phoneno{self.__phoneno}"


class CompCustomer(Customer):
    def __init__(self, id, name, email, creditClass, disc, plan,relMan,creditLine,extension,lstOfNum):
        super(self).__init__(id, name, email, creditClass, disc, plan)
        self.__relMan=relMan
        self.__creditLine=creditLine
        self.__extension=extension
        self.__lstOfNum=lstOfNum
    def __str__(self):
        return  Customer.__str__(self)+f"relMan:{self.__relMan}+creditLine:{self.__creditLine}+extension{self.__extension} lstof num{self.__lstOfNum}"