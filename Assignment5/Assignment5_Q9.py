lst = ["aaaa", "sgkgafnk", "fgfh", "g"]

# For fn=ind the string greater than given number
def filter_long_words(n,lst):
    lst2 = list(filter(lambda x: len(x) > n,lst))
    print(f"string grater than {n} length {lst2})

# input from user for fin the grater string in list
num = int(input("Enter number : "))
filter_long_words(num,lst)
