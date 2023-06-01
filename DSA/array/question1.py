'''

Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

#defining function

def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    n = len(nums)
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum


nums = list(map(int,input("Enter numbers : ").split()))

target = int(input("Enter target number : "))

print(threeSumClosest(nums,target))