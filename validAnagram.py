# Valid Anagram

# Time Complexity: O(n) -> because we iterate over each of the strings once to build the frequency

# Space Complexity: O(n) -> because we're using two dictionaries to store the frequencies

def isAnagram(s, t):
    characters1 = {}
    characters2 = {}

    for i in s:
        characters1[i] = characters1.get(i, 0) + 1
    for i in t:
        characters2[i] = characters2.get(i, 0) + 1
    
    if characters1 == characters2:
        return True
    else:
        return False
    

# def isAnagram(s, t):
#     return sorted(s) == sorted(t)
    

s = "rat"
t = "car"

print(isAnagram(s,t))