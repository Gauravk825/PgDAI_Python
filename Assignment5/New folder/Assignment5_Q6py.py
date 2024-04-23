# for creating new set
def creat_set(ans):
    set2 = set((x for x in ans.split()))
    return set2

# for removing the given vlue from set
def delete_name(name):
    set1.discard(name)# discard delete value if exists otherwise ingnored
    print(f"Set after deleted {ans} : {set1}")

# for add name into set
def addName(name):
    set1.add(name)
    print(f"Set after name {ans}: {set1}")

# for performing unoin of two sets
def union_set(set1,set2):
    set3 = set1.union(set2)
    print(f"Union of {set1} and {set2} :{set3}")

# for intersection
def intersection_set(set1,set2):
    set3 = set1.intersection(set2)
    print(f"Intersection of {set1} and {set2} :{set3}")
# for diffirence of two sets  
def difference_set(set1,set2):
    set3 = set1.difference(set2)
    print(f"Differenceof {set1} and {set2} :{set3}")

# converting set ino frozenset
def frozenset_set(set1):
    set3 = frozenset(set1)
    return set3

set1 = set((y for y in input("Enter names : ").split()))
print(set1)
choice =0
while(choice!=8):
    choice = int(input("""1) Delete element if exists otherwise do not show any err
2) Add a elemet
3) Create one more set
4) Union of 2 sets
5) Intersection of 2 sets
6) Difference of 2 sets
7) Convert set into frozenset
8) Exit """))
    match choice:
        case 1 :
            ans = input("Enter name for delete : ")
            delete_name(ans)
        case 2 :
            ans = input("Enter name to add : ")
            addName(ans)  
        case 3 :
            ans = input("Enter names : ")
            set2 = creat_set(ans)
            print(f"Second set : {set2}")
        case 4 :
            union_set(set1,set2)
        case 5:
            intersection_set(set1,set2)
        case 6 :
            difference_set(set1,set2)
        case 7 :
            set3 = frozenset_set(set1)
            print(f"frozen set : {set3}")
        case 8 :
            print("Thank you for visiting....")
        case _ :
            print("Invalid option.")
            
            
