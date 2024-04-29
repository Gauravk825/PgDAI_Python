import sqlite3
import json

def deletedata(eid):
    con=sqlite3.connect(r"C:\Users\Administrator.DAI-PC2\Desktop\Python\SQL_conect\mydb.db")
    cursor=con.cursor()
    cursor.execute("delete from employee where eid=?",(eid,))
    con.commit()
    cursor.close()
    con.close()
    return True
def modifyemployee(data):
    con=sqlite3.connect(r"C:\Users\Administrator.DAI-PC2\Desktop\Python\SQL_conect\mydb.db")
    cursor=con.cursor()
    cursor.execute("update employee set ename=?,sal=?,edep=? where eid=?",(data['ename'],data['sal'],data['edep'],data['eid']))
    con.commit()
    cursor.close()
    con.close()
    return True

def addnewemployee(data):
    con=sqlite3.connect(r"C:\Users\Administrator.DAI-PC2\Desktop\Python\SQL_conect\mydb.db")
    cursor=con.cursor()
    cursor.execute("insert into employee values(?,?,?,?)",(data['eid'],data['ename'],data['sal'],data['edep']))
    con.commit()
    cursor.close()
    con.close()
    return True
def findallemployee():
    con=sqlite3.connect(r"C:\Users\Administrator.DAI-PC2\Desktop\Python\SQL_conect\mydb.db")
    cursor=con.cursor()
    cursor.execute("select * from employee")
    rows=cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i] #{"eid":12,"ename":"xxx"}
        result.append(d)
    if len(result)>0:
        #return {"payload":result}
        print(result)
        #convert dictionary into json fomat
        cursor.close()
        con.close()
        return json.dumps(result)
            # return make_response({"payload":result},200)
    else:
        return "No Data Found"
    
    
    
    
    
def getempbyid(eid):
    con=sqlite3.connect(r"C:\Users\Administrator.DAI-PC2\Desktop\Python\SQL_conect\mydb.db")
    cursor=con.cursor()
    cursor.execute("select * from employee where eid=?",(eid,))
    rows=cursor.fetchone()
    # result = []
    # for row in rows:
    #     d = {}
    #     for i, col in enumerate(cursor.description):
    #         d[col[0]] = row[i] #{"eid":12,"ename":"xxx"}
    #     result.append(d)
    # if len(result)>0:
    #     #return {"payload":result}
    #     print(result)
    #     #convert dictionary into json fomat
    #     cursor.close()
    #     con.close()
    con.commit()
    cursor.close()
    con.close()
    return json.dumps(rows)
     
