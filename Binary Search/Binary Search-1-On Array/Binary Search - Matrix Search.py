Problem Description
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.
NOTE: Rows are numbered from top to bottom, and columns are from left to right.


Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6


Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.


Output Format
Return 1 if B is present in A else, return 0.


Example Input
Input 1:
A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3
Input 2:
A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
 3 is present in the matrix at A[0][1] position so return 1.
Explanation 2:
 3 is not present in the matrix so return 0.

NOTE to try CODE Solution:

 key is to make the 2D as flatterned array i.e as 1D array and then do Binary search


CODE:

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
       
        n = len(A)
        m = len(A[0])
        l = 0
        h = (m * n) - 1

        while l <= h:
            mid = ( l + h ) // 2
            row = mid // m  #tells how many complete rows are crossed in the flattened array.
            column = mid % m   #tells where you land in the current row.
           
            if A[row][column] < B:
                l = mid + 1

            elif A[row][column]>B:
                h = mid - 1

            else:
                return 1

        return 0
