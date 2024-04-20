# 1) Reverse the string
lst = [100, 200, 300, 400, 500] # list assignment

print(f"List before reverse:{lst}")
lst.reverse()
print("List after reverse: ", lst)
print("********************************************")

      
#2) # Concatnate two string index-wise
lst1 = ["M", "na", "i", "Raj"]
lst2 = ["y", "me", "s", "esh"]

for n,n1 in zip(lst1,lst2): #[(10,"Pune"),(20,"mumbai")....]
    print(f"{n}{n1}", end=" ")
    
print()

print("*******************************************")
#3) Turn evry item of list into its sqare

alst = [1,2,3,4,5,6,7]
i=0
for n in alst:
    alst[i] = n**2
    i+=1

print(alst)

print("********************************************")

#4) Concatenate two lists in the following order
''''list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
output:
['Hello Students ', 'Hello Sir', 'welcome Students ', 'Welcome Sir']
'''
list1 = ["Hello", "Welcome"]
list2 = ["Students", "Sir"]
list3 = []

for string1 in list1:
    for string2 in list2:
        list3.append(string1+" "+string2)

print(f"Concatenated list is {list3}")

print("********************************************")
#5)Iterate both lists simultaneously such that list1 should display item
#in original order and list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
i=0
for n in list1:
    print(list1[i],list2[i])
    i+=1

print("********************************************")
#6)Remove empty strings from the list of strings


list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
str1 = ""
while str1 in list1 :
    list1.remove(str1)
print(list1)
print("********************************************")

#7Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#8)
list1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(['h','j','k'])
print(list1)
print("********************************************")

#9)
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 100
print(list1)
print("********************************************")

#10)

list1 = [5, 20, 15, 20, 25, 50, 20]
num = 20
while num in list1:
    list1.remove(num)


print(list1)


