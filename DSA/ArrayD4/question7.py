'''

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] 

should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations

Example 1:

Input: m = 3, n = 3, ops = [[2,2],[3,3]]

Output: 4

Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.


'''

def maxCount(m, n, ops):
    
    if not ops:
        return m * n
    
    min_row = float('inf')
    min_col = float('inf')
    
    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])
    
    return min_row * min_col


m =int(input("Enter the number of rows : "))

n =int(input("Enter the number of coloumns : "))

ops=[]

num_operations = int(input("Enter the number of operations: "))

for _ in range(num_operations):

    ai = int(input("Enter ai: "))
    bi = int(input("Enter bi: "))

    ops.append([ai, bi]).split()

result = maxCount(m, n, ops)

print(result)
