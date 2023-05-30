'''
Q8. You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example

Input: nums = [1,2,2,4]

Output: [2,3]

'''


def lostDigit(nums):

    n=len(nums)
    l =[]
    num_set = set()

#check dulicate value

    for num in nums:
        if num in num_set:
            print(num)
            l.append(num)
        else:
            num_set.add(num)

#check missing number

    total_sum = (n * (n + 1)) // 2  # Sum of numbers from 1 to n

    given_sum = sum(num_set)  # Sum of given set of numbers

    missing_number = total_sum - given_sum
    
    l.append(missing_number)

    return l



   
#taking inputs

nums = list(map(int, input("Enter nums : ").split()))

#calling function

digits = lostDigit(nums)

print(digits)