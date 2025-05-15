Problem Description
Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.


Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000


Input Format
First argument is a 2D matrix of integers.


Output Format
You have to return the Transpose of this 2D matrix.


Example Input
Input 1:
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Input 2:
A = [[1, 2],[1, 2],[1, 2]]


Example Output
Output 1:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output 2:
[[1, 1, 1], [2, 2, 2]]


Example Explanation
Explanation 1:
Clearly after converting rows to column and columns to rows of [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
 we will get [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
Explanation 2:
After transposing the matrix, A becomes [[1, 1, 1], [2, 2, 2]]


=================================
CODE with space complexity:
==================================
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        #every element oafter transpose gets swapped i.e (i,j) becomes (j,i)
        
        mat=[[0]*len(A) for _ in range(len(A[0]))]
        for i in range(len(A)):
            
            for j in range(len(A[0])):
                mat[j][i]=A[i][j]
        return mat


=================================
CODE without space complexity:
==================================
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        #every element oafter transpose gets swapped i.e (i,j) becomes (j,i)
     n = len(A)
     
     for i in range(n):
      #makesure to rotate colum from (i+1) to lenghtof columns i.e len(A[0])
      for j in range(i+1, n):
       
            #if we rotate every elemtn then it becomes origin  matrix element 
       A[j][i], A[i][j] = A[i][j], A[j][i]
       
     return A

