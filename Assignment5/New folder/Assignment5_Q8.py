def insert_string(string_list, new_string):
  # Find the index of the first string with the same second character as the new string.
  for i, string in enumerate(string_list):
    if string[1] == new_string[1]:
      # Insert the new string at the current index.
      string_list.insert(i, new_string)
      return string_list

  # If no string with the same second character is found, append the new string to the end.
  string_list.append(new_string)
  return string_list

# Initialize the list
string_list = ['dxz', 'axz', 'bat', 'rat', 'cat', 'pat', 'bbc', 'bbm', 'cbm', 'dcm']

# Insert "sat"
string_list = insert_string(string_list, 'sat')

# Insert "pick"
string_list = insert_string(string_list, 'pick')

# Print the final list
print(string_list)