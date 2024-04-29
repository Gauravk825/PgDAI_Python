from flask import Flask,request
from Employeeao.employeecurd import *
app=Flask(__name__)

@app.route("/employees",methods=['GET'])
def getallproducts():
    return findallemployee()

@app.route('/employees',methods=['POST'])
def addproduct():
    #data=request.json()
    print(request.form['eid'])
    data=request.form
    #print(request.json['pname'])
    #print(data)
    addnewemployee(data)
    return "added successfully"

@app.route('/employees/<eid>',methods=['PUT'])
def updateproduct(eid):
    print("in put",eid)
    data=request.form
    #print(request.json['pid'])
    #print(data)
    modifyemployee(data)
    return "updated successfully"

@app.route('/employees/<eid>',methods=['DELETE'])
def deleteproduct(eid):
    print("in delete ",eid)
    deletedata(eid)
    return "deleted successfully"

@app.route('/employees/<eid>',methods=['GET'])
def getbyid(eid):
    print("Data For Id : ",eid)
    print(request.form['eid'])
    data=request.form
    return getempbyid(eid)
    
    
    #return "Get successfully"

if __name__=="__main__":
    app.run()