Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.


Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000


Input Format
First argument is an integer array A.


Output Format
Return an integer denoting the minimum time to make all elements equal.


Example Input
A = [2, 4, 1, 3, 2]


Example Output
8


Example Explanation
We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.


======================================
  CODE:
======================================

class Solution:
    
    def solve(self, A):
      """Returns the minimum operations needed to make all elements equal to the max value."""
      # @param A : list of integers
      # @return an integer
      
      # Get Max value in the array
      mx = A[0]

      for i in range(1, len(A)):
        
        if mx < A[i]:
          mx = A[i]

      # Iterate over array
      result = 0
      for i in range(len(A)):
        # Difference from max over each element is number of opearation needed for making values equal
        result += mx - A[i]

      return result 
