'''

First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.

'''


#defining function


def unique(s):



    # creating hashmap

    frequency={}


    # finding frequency of each charachter in string

    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1


    # finding first charachter with frequency 1 - unique charachter in string

    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i


    # returning value in absesnce of unique charachter.
   
    return -1



# taking input

s=input("Enter string : ")


# printing result

print(unique(s))
