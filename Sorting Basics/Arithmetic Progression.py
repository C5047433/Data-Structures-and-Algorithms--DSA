Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.


Problem Constraints
2 <= N <= 10^5
-10^9 <= A[i] <= 10^9


Input Format
The first and only argument is an integer array A of size N.


Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.


Example Input
Input 1:
 A = [3, 5, 1]
Input 2:
 A = [2, 4, 1]


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:
 We can reorder the elements as [1, 3, 5] or [5, 3, 1] with differences 2 and -2 respectively, between each consecutive elements.
Explanation 2:
 There is no way to reorder the elements to obtain an arithmetic progression.

Hint to Solve:
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

============================================
CODE:
============================================
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
       # Step 1: Sort the array to check in order
        A.sort()
        
        n = len(A)
        if n <= 2:
            return 1  # Any list of size 0, 1, or 2 is an AP

        # Step 2: Calculate the common difference
        common_diff = A[1] - A[0]

        # Step 3: Check all consecutive differences
         for i in range(2, n):
            if A[i] - A[i - 1] != common_diff:
                return 0  # Not an AP

         return 1  # All differences matched → it's an AP



Example Test:
s = Solution()
print(s.solve([3, 5, 1]))     # Output: 1 (after sorting: [1,3,5], diff = 2)
print(s.solve([1, 2, 4]))     # Output: 0
Let me know if you'd like a version that doesn't require sorting (e.g., for performance-sensitive code)!




      
