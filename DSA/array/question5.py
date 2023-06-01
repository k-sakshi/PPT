'''

You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''


#defining function

def plusOne(digits):

    n = len(digits)

    result = []

    carry = 1

    for i in range(n-1, -1, -1):
        digit_sum = digits[i] + carry
        result.append(digit_sum % 10)
        carry = digit_sum // 10

    if carry == 1:
        result.append(1)
    result.reverse()

    return result


#taking input

nums = list(map(int,input("Enter numbers : ").split()))

print(plusOne(nums))