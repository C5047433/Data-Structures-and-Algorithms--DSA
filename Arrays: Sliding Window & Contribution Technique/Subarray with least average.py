Problem Description
Given an array A of size N, find the subarray of size B with the least average.


Problem Constraints
1 <= B <= N <= 10^5
-10^5 <= A[i] <= 10^5


Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.


Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.


Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:
A = [3, 7, 5, 20, -10, 0, 12]
B = 2


Example Output
Output 1:
3
Output 2:
4


Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:
 Subarray between [4, 5] has minimum average



========================================
CODE:
========================================

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        Returns the starting index of the subarray of length B with the minimum sum.
        """
        n = len(A)
        if n < B:
            return -1  # Not enough elements for one window
          
        result = 0
        min_sum = sum(A[0:B])
    
        avg = min_sum
        start = 0
        end = B
        while end < n:
            min_sum += A[end] - A[start]
            if min_sum < avg:
                avg = min_sum
                result = start + 1
            end += 1
            start += 1
        return result 



Example test: 
s = Solution()
print(s.solve([3, 7, 90, 20, 10, 50, 40], 3))  # Output: 3
  


  

