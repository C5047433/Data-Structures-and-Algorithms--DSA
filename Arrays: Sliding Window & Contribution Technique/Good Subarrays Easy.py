Problem Description
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.


Problem Constraints
1 <= len(A) <= 5 x 103
1 <= A[i] <= 103
1 <= B <= 107


Input Format
The first argument given is the integer array A.
The second argument given is an integer B.


Output Format
Return the count of good subarrays in A.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 4
Input 2:
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65


Example Output
Output 1:
6
Output 2:
36


Example Explanation
Explanation 1:
Even length good subarrays = {1, 2}
Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5} 
Explanation 1:
There are 36 good subarrays



======================================
CODE:
======================================

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
      n = len(A)
      count = 0
      # Iterate over all possible start indices of subarrays
      for si in range(n):
        current_sum = 0
        # For each start index, extend the subarray to all possible end indices
        for ei in range(si, n):
          # Add the current element to the running sum of the subarray
          current_sum += A[ei]
          # Check subarray conditions:
          # - If length is even and sum is less than B, count it

          if (ei - si + 1) % 2 == 0 and current_sum < B:
            count += 1

          # - If length is odd and sum is greater than B, count it
          elif (ei - si + 1) % 2 != 0 and current_sum > B:
            count += 1
            
      return count
