Problem Description
Given an array A of length N, return the subarray from B to C.


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B <= C < N


Input Format
The first argument A is an array of integers
The remaining argument B and C are integers.


Output Format
Return a subarray


Example Input
Input 1:
A = [4, 3, 2, 6]
B = 1
C = 3
Input 2:
A = [4, 2, 2]
B = 0
C = 1


Example Output
Output 1:
[3, 2, 6]
Output 2:
[4, 2]


Example Explanation
Explanation 1:
The subarray of A from 1 to 3 is [3, 2, 6].
Explanation 2:
The subarray of A from 0 to 1 is [4, 2].




============================================
CODE:
============================================

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

      result = []

      # Iterate in the range from B to C+1 and append to result and return 
      for i in range(B, C+1):
        result.append(A[i])

      return result

        
