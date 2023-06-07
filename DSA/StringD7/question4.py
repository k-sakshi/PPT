'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

'''
def reverce(str):
    
    rev_str=[]

    word_list =list(str.split(' '))

    for word in word_list:
        rev_str.append(word[::-1])
        
    
    return (" ".join(rev_str))


str = input("Enter string : ")

reverse_str = reverce(str)

print(reverse_str)
