'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 

then reverse the first k characters and leave the other as original.

Example

Input: s = "abcdefg", k = 2

Output: bacdfeg

'''

def reverseString(s, k):

    if k <= 0:

        return s

    chars = list(s)

    n = len(chars)

    for i in range(0, n, 2 * k):

        left = i
        
        right = min(i + k - 1, n - 1)

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return ''.join(chars)


s= input("Enter string : ")

k= int(input("Enter no of charachters : "))

result = reverseString(s, k)

print(result)
