'''
Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 

You must also not convert the inputs to integers directly.


Input: num1 = "11", num2 = "123"

Output:**

"134"

'''

def add(num1,num2):

    n1, n2 = len(num1), len(num2)
    carry = 0
    result = []

    i, j = n1 - 1, n2 - 1

    while i >= 0 or j >= 0 or carry:

        digit1 = int(num1[i]) if i >= 0 else 0

        digit2 = int(num2[j]) if j >= 0 else 0

        current_sum = digit1 + digit2 + carry

        carry = current_sum // 10

        digit_sum = current_sum % 10

        result.append(str(digit_sum))

        i -= 1
        
        j -= 1

    return ''.join(result[::-1])




num1 =input("First number : ")

num2 =input("Second number : ")

sum =add(num1,num2)

print(sum)