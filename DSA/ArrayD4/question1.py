'''

Question 1

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared 

in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

Explanation: Only 1 and 5 appeared in the three arrays.


'''

#defining function

def commonNumbers(arr1,arr2,arr3):

    #converting array to set

    arr1 = set(arr1)
    arr2 = set(arr2)
    arr3 = set(arr3)

    #taking intersection of all three set of array

    result = arr1.intersection(arr2, arr3)
    

    #returning result in list

    return(list(result))


#taking input


arr1 = list(map(int,input("Enter first array : ").split()))
arr2 = list(map(int,input("Enter second array : ").split()))
arr3 = list(map(int,input("Enter third array : ").split()))

#printing result

result = (commonNumbers(arr1,arr2,arr3))

print(sorted(result))