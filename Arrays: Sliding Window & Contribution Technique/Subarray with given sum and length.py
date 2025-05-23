Problem Description
Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^4
1 <= B <= N
1 <= C <= 10^9


Input Format
First argument A is an array of integers.
The remaining arguments B and C are integers


Output Format
Return 1 if such a subarray exist and 0 otherwise


Example Input
Input 1:
A = [4, 3, 2, 6, 1]
B = 3
C = 11
Input 2:
A = [4, 2, 2, 5, 1]
B = 4
C = 6


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
The subarray [3, 2, 6] is of length 3 and sum 11.
Explanation 2:
There are no such subarray.


===============================================
CODE:
===============================================

class Solution:
    """
    A : list of integers
    B : integer (window size)
    C : integer (target sum)
    Returns 1 if a window of size B with sum C exists, else 0.
    """
    def solve(self, A, B, C):

      n = len(A)
      found = 0
      if n == 1:
        if A[0] == C:
          found = 1
      
      else:
        current_sum = 0
        for i in range(B):
          current_sum += A[i]

          if current_sum == C:
            found = 1

        window_sum = current_sum

        i = 0
        j = B

        while j < n:
          window_sum -= A[i]
          window_sum += A[j]

          if window_sum == C:
            found = 1
          i += 1
          j += 1
      return found

          

        
