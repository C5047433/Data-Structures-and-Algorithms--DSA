Problem Description
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.


Problem Constraints
1 <= N <= 10^5
-109 <= A[i] <= 10^9


Input Format
First argument A is an integer array.


Output Format
Return the sum of maximum and minimum element of the array


Example Input
Input 1:
A = [-2, 1, -4, 5, 3]
Input 2:
A = [1, 3, 4, 1]


Example Output
Output 1:
1
Output 2:
5


Example Explanation
Explanation 1:
Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1. 
Explanation 2:
Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.





=====================================================
CODE:
=====================================================


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
      # Initilize mn to A[0]
      mn = A[0]

      # Iterate over array from position 1 to end 
      for i in range(1, len(A)):

         #if any element is less then assign it to mn 
        if A[i] < mn:
          mn = A[i]

      mx = A[0]

      # Iterate over array from position 1 to end 
      for i in range(1, len(A)):

        # if any element is greater then assign it to mx
        if A[i] > mx:
          mx = A[i]

      return mn + mx 
