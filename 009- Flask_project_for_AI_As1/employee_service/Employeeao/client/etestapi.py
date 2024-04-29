import requests

print("send get request")
response = requests.get("http://127.0.0.1:5000/employees")
print(response)
print(response.content) # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
print(response.json()) # This method is convenient when the API returns JSON


print("send put request")
response = requests.put('http://127.0.0.1:5000/employees/101', data = {'eid':105,'ename':'shyam','sal':34000,'edep':'HR'})
print(response.content)


print("send delete request")
response = requests.delete('http://127.0.0.1:5000/employees/101', data = {'eid':104,'ename':'gaurav','sal':34,'edep':'data_sci' })
print(response.content)



print("send post request")
response = requests.post('http://127.0.0.1:5000/employees', data = {'eid':106,'ename':'xxx','sal':34,'edep':'associate'})
print(response)
print(response.content)

print("send get request by Id")
response = requests.get("http://127.0.0.1:5000/employees/105", data = {'eid':105,'ename':'shyam','sal':34000,'edep':'HR'})
print(response)
print(response.content) # Return the raw bytes of the data payload
#print(response.text()) # Return a string representation of the data payload
#print(response.json()) # This method is convenient when the API returns JSON


# Update an existing resource
#requests.put('http://127.0.0.1:5000/products', data = {'key':'value'})h