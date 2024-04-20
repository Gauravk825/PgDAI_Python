#Q1
aTuple = (10, 20, 30, 40, 50,60)
print(aTuple)
aTuple = list(aTuple) # converting data type tuple into list
aTuple.reverse() # reversing the list
print(tuple(aTuple))
print("********************************************")

#Q2. display value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])
print("********************************************")

#Q3. Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(a, b, c, d)
print("********************************************")

#Q4.Swap the following two tuples
##tuple1 = (11, 22)
##tuple2 = (99, 88)
##Expected output:
##tuple1 = (99, 88)
##tuple2 = (11, 22)

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1  #swapping the tuples
print(tuple1, tuple2)
print("********************************************")

#Q5.Copy element 44 and 55 from the following tuple into a new tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple1[tuple1.index(44)]
#copying the tuple value using index function in new tuple
tuple2 = tuple1[tuple1.index(44)], tuple1[tuple1.index(55)]   
print(tuple2)
print("********************************************")


#Q6.Modify the first item (22) of a list inside a following tuple to 200
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 200 #rewriting 22 into 200
print(tuple1)


