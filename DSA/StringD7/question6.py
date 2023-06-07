'''
Given two strings s and goal, return true if and only if s can become  goal after some number of shift on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

Example 1:

Input: s = "abcde", goal = "cdeab"

Output: true

'''


def rotateString(s, goal):

    if len(s) != len(goal):

        return False

    if s == goal:
        return True

    for _ in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            return True

    return False



s = input("Enter the first string: ")

goal = input("Enter the second string: ")

result = rotateString(s, goal)

print(result)