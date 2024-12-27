Problem Description

Given two sorted arrays A and B of size M and N respectively, return the median of the two sorted arrays.
Round of the value to the floor integer [2.6=2, 2.2=2]


Problem Constraints

0 <= M <= 10^5
0 <= N <= 10^5
-10^9 <= A[i], B[i] <= 10^9


Input Format

First argument A is an array of integers.
First argument B is an array of integers.


Output Format

Return an integer.


Example Input

Input 1:

A = [1, 3]
B = [2]

Input 2:

A = [1, 2]
B = [3,4]


Example Output

Output 1:
3


Output 2:
3


Example Explanation

Example 1:
merged array = [1,2,3] and median is 2.

Example 2:
merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2


import math
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        if len(A) > len(B):
            return self.solve(B, A)

        n1 = len(A)
        n2 = len(B)

        N = n1 + n2

        l = 0
        h = n1
        while l <=h :
            mid = (l+h)//2

            cut1 = mid
            cut2 = N//2 - cut1

            l1 = float('-inf') if cut1 == 0 else A[cut1-1]
            l2 = float('-inf') if cut2 == 0 else  B[cut2-1]
            r1 = float('inf') if  cut1 == n1 else A[cut1] 
            r2 = float('inf') if cut2 == n2 else B[cut2]


            if l1 <= r2 and l2 <= r1:
                
                if N%2 == 0:
                    return math.floor(max(l1,l2) + min(r1,r2))//2 
                else:
                    return math.floor(min(r1,r2))

            elif l1 > r2:
                h = cut1 - 1

            elif l2 > r1:
                l = cut1 + 1

        return 0