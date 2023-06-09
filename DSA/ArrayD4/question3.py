'''

Given a 2D integer array matrix, return the transpose of  matrix.

The   transpose   of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]


'''
def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    transposed = [[0] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            transposed[j][i] = matrix[i][j]

    return transposed

n =int(input("Enter the number of rows : "))

matrix =[]

for row in range(n):
     row = list(map(int,input().split()))
     matrix.append(row)

result = transpose(matrix)

print(result) 