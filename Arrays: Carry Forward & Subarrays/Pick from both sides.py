Problem Description
You are given an integer array A of size N.
You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
Find and return the maximum possible sum of the B elements that were removed after the B operations.
NOTE: Suppose B = 3, and array A contains 10 elements, then you can:
Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.


Problem Constraints
1 <= N <= 10^5
1 <= B <= N
-103 <= A[i] <= 10^3


Input Format
First argument is an integer array A.
Second argument is an integer B.


Output Format
Return an integer denoting the maximum possible sum of elements you removed.


Example Input
Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:
 A = [ 2, 3, -1, 4, 2, 1 ]
 B = 4


Example Output
Output 1:
 8
Output 2:
 9


Example Explanation
Explanation 1:
 Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:
 Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9


======================================================
CODE:
======================================================

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        Finds the maximum sum of B elements picked from either end of the array.
    
        Args:
        A (list[int]): List of integers.
        B (int): Number of elements to pick.
    
        Returns:
        int: Maximum sum possible by selecting B elements from either end.
        """

        n = len(A)

        # Edge case:
        if B == 0:
            return 0

        if B > n:
            return -1
          
        # Initialize and calculate prefix sum of array
        prefix_sum = [0] * n
        prefix_sum[0] = A[0]

        for i in range(1, n):
            prefix_sum[i] = A[i] + prefix_sum[i - 1]

        # Initialize and calculate sufix sum of array
        suffix_sum = [0] * n
        suffix_sum[n - 1] = A[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = A[i] + suffix_sum[i + 1]

        #removing B elements from both the side 
        result = max(prefix_sum[B - 1], suffix_sum[n - B])

        #try picking B elemetns from either sides
        for i in range(1, B):
            result = max(result, prefix_sum[i - 1] + suffix_sum[n - B + i])

        return result
