Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

Input Format
The only argument given is string A.
Output Format
Return the length of the longest consecutive 1’s that can be achieved.
Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example
Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7



==========================================
CODE:
==========================================

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        """
        Finds the maximum number of consecutive 1s possible 
        in a binary string after flipping at most one 0 to 1.
        """
        n = len(A)
        max_consecutive = 0
        total_ones = 0

        for i in range(n):
            if int(A[i]) == 0:
                left_ones = 0
                right_ones = 0

                # Count 1s to the left of the 0
                j = i - 1
                while j >= 0 and int(A[j]) == 1:
                    j -= 1
                    left_ones += 1

                # Count 1s to the right of the 0
                j = i + 1
                while j < n and int(A[j]) == 1:
                    j += 1
                    right_ones += 1

                max_consecutive = max(max_consecutive, left_ones + right_ones)
            else:
                total_ones += 1

        # If all characters are 1s, return total length
        if total_ones == n:
            return n

        # Flip one 0 to 1 if possible
        if max_consecutive < total_ones:
            max_consecutive += 1

        return max_consecutive

