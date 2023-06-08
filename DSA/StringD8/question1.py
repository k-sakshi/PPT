'''
Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

Input: s1 = "sea", s2 = "eat"

Output: 231

Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

Deleting "t" from "eat" adds 116 to the sum.

At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

'''

def minimumDeleteSum(s1, s2):

    m = len(s1)
    n = len(s2)
    
    # Create a 1D table to store the minimum ASCII sum

    dp = [0] * (n + 1)
    
    # Fill the table

    for j in range(1, n + 1):
        dp[j] = dp[j - 1] + ord(s2[j - 1])
    
    # Calculate the minimum ASCII sum

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] += ord(s1[i - 1])
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
            prev = temp
            
    
    return dp[n]


s1 = input("Enter first string : ")

s2 = input("Enter second string : ")

result = minimumDeleteSum(s1, s2)

print(result)  