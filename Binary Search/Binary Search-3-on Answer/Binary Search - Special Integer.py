Problem Description

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.



Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9


Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the maximum value of K (sub array length).

Example Input

Input 1:
A = [1, 2, 3, 4, 5]
B = 10

Input 2:
A = [5, 17, 100, 11]
B = 130


Example Output
Output 1:
 2

Output 2:
 3

Example Explanation

Explanation 1:

For K = 5, There are subarrays [1, 2, 3, 4, 5] which has a sum > B
For K = 4, There are subarrays [1, 2, 3, 4], [2, 3, 4, 5] which has a sum > B
For K = 3, There is a subarray [3, 4, 5] which has a sum > B
For K = 2, There were no subarray which has a sum > B.
Constraints are satisfied for maximal value of 2.
Explanation 2:

For K = 4, There are subarrays [5, 17, 100, 11] which has a sum > B
For K = 3, There were no subarray which has a sum > B.
Constraints are satisfied for maximal value of 3.

NOTE: 
Use Sliding window + Bianry search Technique 

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def max_window_size(self, A, B):
        l = 0
	    h = len(A)
        result = mid 

	while l <= h :
        mid = (l + h) // 2

        subarray_status = self.sum_of_subarray(A, mid, B)
        if subarray_status:
            l = mid + 1
            result = mid
        else:
            h = mid - 1
    return result

    
    def sum_of_subarray(self, A, mid, B):
        current_sum = 0

        for i in range(mid):
            current_sum +=A[i]

        if current_sum > B:
            return False

        i = 0
        j = mid
        while j < len(A):
            current_sum -=A[i]
            current_sum +=A[j]

            if current_sum > B:
                return False
            else:
                i +=1
                j +=1
        return True


