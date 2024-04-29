class Student :
    
    
    #Student constructor
    def __init__(self, studid = 0, name = "", m1 = 0, m2 = 0, m3 = 0, gpa = 0.0) :
        self.__studid = studid
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__gpa = Student.calculategpa(self.__m1,self.__m2, self.__m3)
    
    # printing string
    def __str__(self) :
        return f"Student Id: {self.__studid} \nName : {self.__name} \nM1 : {self.__m1} \nM2 : {self.__m2} \nM3 : {self.__m3}"
    # setters
    def __setstudid(self, id) :
        self.__studid = id
        
    def __setname(self, nm) :
        self.__name = nm
        
    def __setm1(self, mi) :
        self.__m1 = mi
        
    def __setm2(self, mj) :
        self.__m2 = mj
        
    def __setm3(self, mk) :
        self.__m3 = mk

     #getters    
    def getstudid(self) :
        return self.__studid
    
    def getname(self) :
        return self.__name
    
    def getm1(self) :
        return self.__m1
    
    def getm2(self) :
        return self.__m2
    
    def getm3(self) :
        return self.__m3
    
    def getgpa(self) :
        return self.__gpa
    
    #function to calculate gpa
    def calculategpa(m1, m2, m3) :
        return float((1/3) *m1 + (1/2) *m2 +(1/4)*m3)