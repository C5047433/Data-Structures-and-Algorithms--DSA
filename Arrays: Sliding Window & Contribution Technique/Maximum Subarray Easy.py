Problem Description
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.


Problem Constraints
1 <= A <= 10^3
1 <= B <= 10^9
1 <= C[i] <= 10^6


Input Format
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.


Output Format
Return a single integer which denotes the maximum sum.


Example Input
Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
Input 2:
A = 3
B = 1
C = [2, 2, 2]


Example Output
Output 1:
12
Output 2:
0


Example Explanation
Explanation 1:
We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
Explanation 2:
All elements are greater than B, which means we cannot select any subarray.
Hence, the answer is 0.


=====================================================
  CODE:
====================================================

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
         """
        Counts the number of subarrays with a sum less than B.

        Args:
        A (list[int]): List of integers.
        B (int): Threshold sum.

        Returns:
        int: Count of subarrays with a sum less than B.
        """

        #Carry forward technique
  
        ans = 0
        for si in range(A):
            currentsum = 0
            for ei in range(si,A):
                currentsum += C[ei]
                
                #Check if any subarray sume is less than or eqauls B, 
                if currentsum <= B:
                    
                    ans = max( currentsum, ans )     # max sum among all these summ less than B
        return ans
