class Friends :
    
    cnt=1
    @staticmethod
    def __generatecode(ftype):
        fid = ftype + str(Friends.cnt)
        Friends.cnt=Friends.cnt+1
        return fid
    
    def __init__(self, name = "", lastname = "", hobbies = [], mobno = "", bdate = "", address = "", fid = "f") :
        
        self.__fid=Friends.__generatecode(fid)
        self.__name = name
        self.__lastname = lastname
        self.__hobbies = hobbies
        self.__mobno = mobno
        self.__bdate = bdate
        self.__address = address
        
    def getid(self) :
        return self.__fid
    
    def getname(self) :
        return self.__name
    
    def getlastname(self) :
        return self.__lastname
    
    def gethobbies(self) :
        return self.__hobbies
    
    def getmobno(self) :
        return self.__mobno
    
    def getbdate(self) :
        return self.__bdate
    
    def getaddress(self) :
        return self.__address
    
    def setname(self, nm) :
        self.__name = nm
        
    def setlastname(self, lsnm) :
        self.__lastname = lsnm
        
    def sethobbies(self, hb) :
        self.__hobbies = hb
        
    def setmobno(self, mb) :
        self.__mobno = mb
        
    def setbdate(self, bd) :
        self.__bdate = bd
        
    def setaddress(self, adr) :
        self.__address = adr
        
    def __str__(self) :
        return f"Id: {self.__fid} Name: {self.__name} Last Name : {self.__lastname} Hobbies : {self.__hobbies} Mobile Number : {self.__mobno} Birth Date : {self.__bdate} Address : {self.__address}"
        
        
if __name__=="__main__":
    
    ob = Friends("Rahul", "Dravid", ["Cricket", "Sports", "Movies"], "9876543289", "12-05-2024", "Mumbai")
    print(ob)
    
        