# fuction for print histrogram
def histogram(lst):
    for i in range(len(lst)): 
        print("*"*lst[i],end="")
        print()

lst = [4,9,7] # given list
histogram(lst) #calling function

