
str1 = input(" Enter text : ") # input string from user
sI= 'AEIOUaeiou'

#function translate text into "rövarspråket"
def translate(str1):
    result =""
    for ch in str1:
        if ch.isalpha():
            if ch in sI:
                result = result +ch
            else :
                result = result+ch+'o'+ch
        else:
            result = result + ch
    return result


print(f"translation of {str1}  into rövarspråket is {translate(str1)}")
