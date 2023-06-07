'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 

Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

Output: true

'''

def checkStraightLine(coordinates):

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):

        x, y = coordinates[i]

        if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
            
            return False

    return True


# taking input

coordinates = []

n = int(input("Enter the number of points: "))

for _ in range(n):

    x = int(input("Enter x-coordinate: "))
    y = int(input("Enter y-coordinate: "))
    coordinates.append([x, y])

result = checkStraightLine(coordinates)

print(result)