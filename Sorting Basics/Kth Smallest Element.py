Problem Description
Find the Bth smallest element in given array A .
NOTE: Users should try to solve it in less than equal to B swaps.


Problem Constraints
1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 10^9


Input Format
The first argument is an integer array A.
The second argument is integer B.


Output Format
Return the Bth smallest element in given array.


Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3
Input 2:
A = [1, 2]
B = 2


Example Output
Output 1:
 2
Output 2:
 2


Example Explanation
Explanation 1:
 3rd element after sorting is 2.
Explanation 2:
 2nd element after sorting is 2.


======================================
CODE using simple sorting:
=======================================
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
	A = list(A)
	A.sort()
	return A[B - 1]


========================================
CODE using SELECTION SORT:
========================================

class Solution:
    def kthsmallest(self, A, B):
        # Step 1: Implement selection sort until B-th smallest is found
        for i in range(len(A)):
            min_idx = i  # Assume the current i is the smallest

            # Step 2: Find the index of the minimum element in remaining array
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j

            # Step 3: Swap the current element with the found minimum
            A[i], A[min_idx] = A[min_idx], A[i]

        # Step 4: Return the k-th smallest element (1-based index)
        return A[B - 1]

