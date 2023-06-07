'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example:

Input: s = "egg", t = "add"

Output: true

'''

#defining function: 


def isomorphicString(s,t):

       
    if len(s) != len(t):
        return False

    char_map_s = {}
    char_map_t = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in char_map_s:
            if char_map_s[char_s] != char_t:
                return False
        else:
            char_map_s[char_s] = char_t

        if char_t in char_map_t:
            if char_map_t[char_t] != char_s:
                return False
        else:
            char_map_t[char_t] = char_s

    return True



#taking input


s=input("Enter first string : ")

t=input("Enter second string : ")

result = isomorphicString(s,t)

print(result)
