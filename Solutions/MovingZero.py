'''
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

'''

# defining function

def moveZero(nums):

    # Index to place the next zero

    zero_index = 0  


    # Move all nonzero elements to the left

    for i in range(len(nums)):

        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1
        
            

# taking input 
nums = list(map(int, input("Enter digits : ").split()))


# calling function
moveZero(nums)

#printing result
print(nums)
