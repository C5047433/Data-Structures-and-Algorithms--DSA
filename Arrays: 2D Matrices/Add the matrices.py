Problem Description
You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
The Following will give you an idea of matrix addition:

Problem Constraints
1 <= A.size(), B.size() <= 1000 1 <= A[i].size(), B[i].size() <= 1000 1 <= A[i][j], B[i][j] <= 1000
Input Format
The first argument is the 2D integer array A The second argument is the 2D integer array B
Output Format
You have to return a vector of vector of integers after doing required operations.
Example Input
Input 1:
A = [[1, 2, 3],   
     [4, 5, 6],   
     [7, 8, 9]]  

B = [[9, 8, 7],   
     [6, 5, 4],   
     [3, 2, 1]]
 
Input 2:
A = [[1, 2, 3],   
     [4, 1, 2],   
     [7, 8, 9]]  

B = [[9, 9, 7],   
     [1, 2, 4],   
     [4, 6, 3]]
 
Example Output
Output 1:
[[10, 10, 10],   
 [10, 10, 10],   
 [10, 10, 10]]
Output 2:
[[10, 11, 10],   
 [5,   3,  6],   
 [11, 14, 12]]
Example Explanation
Explanation 1:
A + B = [[1+9, 2+8, 3+7],  
         [4+6, 5+5, 6+4],  
         [7+3, 8+2, 9+1]]   
      = [[10, 10, 10],   
         [10, 10, 10],   
         [10, 10, 10]].
Explanation 2:
A + B = [[1+9, 2+9, 3+7],  
         [4+1, 1+2, 2+4],  
         [7+4, 8+6, 9+3]]   
      = [[10, 11, 10],   
         [5,   3,  6],   
         [11, 14, 12]].



=========================================
CODE:
=========================================

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n=len(A)
        m=len(A[0])
        
        # Initialize a matrix of the same size with zeros
        mat=[[0]*m for _ in range(n)]  

        #for each element in A, add to the same postional element in B
        for i in range(n):
            for j in range(m):
                
                mat[i][j]=A[i][j]+B[i][j]
        return mat
