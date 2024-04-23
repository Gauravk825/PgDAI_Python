lst1 = input("enter list1: ")
lst3 = lst1.split()
lst2 = [3,4]

def overlapping(lst1,lst3):
    flag=True
    for n in lst1:
        for m in lst2:
            if m==n:
                flag=True
                break
            else:
                flag=False
    print(flag)
overlapping(lst1,lst2)
