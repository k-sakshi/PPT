'''
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4

'''

#defining function

def solution(nums,target):

    left, right = 0, len(nums)

    #binary search
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return -1


#taking input

nums= list(map(int,input("Enter numbers : ").split()))


target = int(input("Enter target number : "))


print(solution(nums,target))