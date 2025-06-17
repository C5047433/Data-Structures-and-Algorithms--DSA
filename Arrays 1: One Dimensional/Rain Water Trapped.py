Problem Description
Imagine a histogram where the bars' heights are given by the array A. Each bar is of uniform width, which is 1 unit. When it rains, water will accumulate in the valleys between the bars.

Your task is to calculate the total amount of water that can be trapped in these valleys.

Example:

The Array A = [5, 4, 1, 4, 3, 2, 7] is visualized as below. The total amount of rain water trapped in A is 11.


Rain Water Trapped



Problem Constraints
1 <= |A| <= 10^5
0 <= A[i] <= 10^5


Input Format
First and only argument is the Integer Array, A.


Output Format
Return an Integer, denoting the total amount of water that can be trapped in these valleys


Example Input
Input 1:
 A = [0, 1, 0, 2]
Input 2:
A = [1, 2]


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
1 unit is trapped on top of the 3rd element.
Rain Water Histogram
Explanation 2:
No water is trapped.



================================================
CODE:
=================================================

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)

        # Arrays to store the max height to the left and right of each element
        maxleft = [0] * n
        maxright = [0] * n

        # Initialize the first element of maxleft
        maxleft[0] = A[0]
        for i in range(1, n):
            # Max height to the left including current element
            maxleft[i] = max(maxleft[i - 1], A[i])

        # Initialize the last element of maxright
        maxright[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            # Max height to the right including current element
            maxright[i] = max(maxright[i + 1], A[i])

        total_water = 0
        for i in range(n):
            # Water trapped at each index = min(left_max, right_max) - height
            total_water += min(maxleft[i], maxright[i]) - A[i]

        return total_water
