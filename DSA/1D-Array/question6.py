'''
Q6.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

'''

#defining function

def repeatation(nums):
    
    num_set = set()

    for num in nums:
        if num in num_set:

# returning true if number is already present in set       
     
            return True
        
#add number in set from nums 

        num_set.add(num)

    return False


#taking input

nums = list(map(int, input("Enter digits : ").split()))

print(repeatation(nums))