'''
Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

Example 1

Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]

'''

def moveZero(nums):

    zero_index = 0  # Index to place the next zero

    # Move all nonzero elements to the left
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1
        
            

# taking input 

nums = list(map(int, input("Enter digits : ").split()))

moveZero(nums)

print(nums)