def isPalindrome(s):
    newStr = ""
    for i in s:
        if i.isalnum():
            newStr += i.lower()
    
    return newStr == newStr[::-1]
    


s = "a."
print(isPalindrome(s))