Problem Description:
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
Elements which are appearing twice are adjacent to each other.
NOTE: Users are expected to solve this in O(log(N)) time.


Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9


Input Format
The only argument given is the integer array A.


Output Format
Return the single element that appears only once.


Example Input
Input 1:
A = [1, 1, 7]
Input 2:
A = [2, 3, 3]


Example Output
Output 1:
 7
Output 2:
 2


Example Explanation
Explanation 1:
 7 appears once
Explanation 2:
 2 appears once


CODE:

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l = 0
        h = len(A)-1
        while l <= h:
            mid = ( l + h ) // 2
            leftmatches=(( mid > 0) and (A[mid-1] == A[mid]))
            rightmatches=((mid < len(A)-1) and A[mid+1] == A[mid])
            if leftmatches:
                if (mid-1)%2 == 0:
                    l = mid + 1
                    h = mid - 1
            elif rightmatches:
                if mid%2 == 0:
                    l = mid + 1
                else:
                    h= mid - 1
            else:
                return A[mid]


