Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.


Problem Constraints
1 <= N, M <= 10^5
1 <= A[i] <= 10^9
0 <= L <= R < N


Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.


Output Format
Return an integer array of length M where ith element is the answer for ith query in B.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
Input 2:
A = [2, 2, 2]
B = [[0, 0], [1, 2]]


Example Output
Output 1:
[10, 5]
Output 2:
[2, 4]


Example Explanation
Explanation 1:
The sum of all elements of A[0 ... 3] = 1 + 2 + 3 + 4 = 10.
The sum of all elements of A[1 ... 2] = 2 + 3 = 5.
Explanation 2:
The sum of all elements of A[0 ... 0] = 2 = 2.
The sum of all elements of A[1 ... 2] = 2 + 2 = 4.



================================================
CODE:
================================================

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
      """
      Computes the sum of elements in A for given query ranges in B using prefix sums.

      Parameters:
      A (list[int]): The input list of integers.
      B (list[list[int]]): List of queries, where each query contains two indices [l, r].

      Returns:
      list[int]: A list of sums corresponding to each query.
      """


      # Inplace prefix sum 
      for i in range(1, len(A)):
        A[i] = A[i] + A[i-1]

      result = []
      for i in range(len(B)):
        l = B[i][0] # in 2D matrix, first element of subarray is l
        r = B[i][1] # in 2D matrix, second element of subarray is r

        #prefix sum formula psum = A[r] - A[l-1]
        if r == 0:
          psum = A[r]
        else:
          psum = A[r] - A[l-1]
        
        result.append(psum) #append the sum in to array 

      return result

