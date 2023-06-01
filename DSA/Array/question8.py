'''
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

Example 1:
Input: nums = [1], k = 0
Output: 0

Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

'''

#defining function

def minimumScore(nums, k):

    min_num = float('inf')
    max_num = float('-inf')

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    return min(max_num - k, min_num + k)

#taking input

nums= list(map(int,input("Enter numbers : ").split()))


k = int(input("Enter integer 'k' : "))


print(minimumScore(nums,k))