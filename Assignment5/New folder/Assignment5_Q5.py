lst=[12,1,2,7,8,5,8]

# for maximum value
max_value = max(lst)
lst1=[]
# for append the -1 to list up to maximum value 
for i in range(max_value+1):
    lst1.append(-1)

# insert index number of previous list in to list
for ind,data in enumerate(lst):
    lst1[data] = ind
print(lst1)
