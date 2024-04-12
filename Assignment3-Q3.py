'''3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a
potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed
under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.'''

str1 = input("Enter the String : ") # input for string
str2 = str1.lower() #change string into lower string
result=""

for ch in str2:
    # removing all punctuation from string and store in new string variable
    if ch.isalpha():
        result = result+ch

if result == result[::-1]: # checking string is plaindrom or not
    print("String is palindrome")
else:
    print("String is not a plindrome" )
