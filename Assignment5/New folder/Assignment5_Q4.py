# taking lit input from user 
lst1 = list((x for x in input("Enter cities : ").split()))
lst2 = list((y for y in input("Enter loctions : ").split()))

# used zip() for caoncanaing to string of two list
lst3 = list(zip(lst1,lst2))
print(lst3)

