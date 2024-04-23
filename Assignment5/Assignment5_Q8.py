# imrt funcltool for reduce functiion
from functools import reduce


lst = ["aaaa", "sgkgafnk", "fgfh", "g"]

# for find the longest string length
def find_longest_word(lst):
    long = reduce(lambda x, y : x if len(x) > len(y) else y, lst)
    print(f"{long} is longest stirn witj length {len(long)}")

find_longest_word(lst)
