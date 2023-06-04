
'''

Convert 1D Array Into 2D Array


You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D)

array with  m rows and n columns using **all** the elements from original.

The elements from indices 0 to n - 1 (**inclusive**) of original should form the first row of the constructed 2D array, the elements from indices 

n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.



Input: original = [1,2,3,4], m = 2, n = 2

Output: [[1,2],[3,4]]


Explanation: The constructed 2D array should contain 2 rows and 2 columns.

The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.

The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.

'''



#defining function

def conversion(arr, m, n):
    if m * n != len(arr):
        print("Impossible to construct the 2D array with the given dimensions.")
        return [[0] * n for _ in range(m)]  # Return empty 2D array if it is impossible

    result = [arr[i*n : (i+1)*n] for i in range(m)]
    print("The 2D array is:")
    return result


# taking input

arr = list(map(int, input("Enter the elements of the 1D array: ").split()))

m = int(input("Enter the number of rows in the 2D array: "))

n = int(input("Enter the number of columns in the 2D array: "))


# Convert 1D array to 2D array

result = conversion(arr, m, n)

# Print the result
1
if result:
    for row in result:
        print(row)
