'''
Q1 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:

Input: 

nums = [2,7,11,15], target = 9

Output0 [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

'''

#defining function


def indices(num,target):
    
    l=[]

    for i in num:

        for j in num:

            if  i >= target or j>=target or i==j :
                continue

            elif i+j== target:
                
                l.append(num.index(i))
                l.append(num.index(j))

                break
        break
            
    return l
                

# taking input 

nums = list(map(int, input("Enter numbers : ").split()))

target =int(input("Enter target number : "))

index=indices(nums,target)

print(index)




