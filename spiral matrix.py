class Solution:
    def spiralmatrix(self, matrix):
        result = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while top < bottom and left < right:
            # Traverse the top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Traverse the right column
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            # Traverse the bottom row (if still within bounds)
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom - 1][i])
                bottom -= 1

            # Traverse the left column (if still within bounds)
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        # Output the spiral order
        print("Spiral Order:", result)


sm=Solution()
matrix=[]
rows=int(input("enter the number of rows"))
cols=int(input("enter the number of cols"))
for i in range (rows):
    while True:
     row=list(map(int,input("enter the elements ").split( )))
     if cols!=len(row):
        print("incorrect matches try again:")
     else:
        matrix.append(row)
        break  
for row in matrix:      
 print(row)        


sm.spiralmatrix(matrix)


