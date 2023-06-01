'''

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


'''

def fourSum(nums, target):

    nums.sort()

    result = []

    n = len(nums)

    for a in range(n - 3):

        if a > 0 and nums[a] == nums[a - 1]:
            continue

        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue

            left = b + 1
            right = n - 1

            while left < right:
                current_sum = nums[a] + nums[b] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[a], nums[b], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

    return result



#taking input 


nums = list(map(int,input("Enter numbers : ").split()))

target = int(input("Enter target number : "))

print(fourSum(nums,target))