dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3={**dict1,**dict2}
print(f"Merge of {dict1} and {dict2} :\n {dict3}")