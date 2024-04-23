word = input("Enter verb : ") # string from user
vowels = 'aeiou'

def make_ing_form(word):
    #check word end with e
    if word.endswith('e') :
        if word == "be" : # if word is be
            word = word+"ing"
        elif word.endswith ("ee") : #if word end with ee
            word = word + "ing"
        elif word.endswith("ie") : # word end with ie
            #string the ie from word
            word = word.rstrip("ie") + 'y' + "ing"
        else :
            word = word.rstrip('e') + "ing"
    elif word[-2] in vowels and word[-3] not in vowels and word[-1] not in vowels:
        word = word + word[-1] + "ing"

    else:
        word = word+"ing"

    print(word)

make_ing_form(word)
