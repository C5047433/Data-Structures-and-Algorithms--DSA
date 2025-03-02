Problem Description
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
Note:
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.


Problem Constraints
1 <= N <= 10^5
-10^5 <= A[i] <= 10^5


Input Format
First arugment is an array A .


Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.


Example Input
Input 1:
A = [-7, 1, 5, 2, -4, 3, 0]
Input 2:
A = [1, 2, 3]


Example Output
Output 1:
3
Output 2:
-1


Example Explanation
Explanation 1:
i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   7
1                  -7                                   6
2                  -6                                   1
3                  -1                                  -1
4                   1                                   3
5                  -3                                   0
6                   0                                   0

3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:
i   Sum of elements at lower indexes    Sum of elements at higher indexes
0                   0                                   5
1                   1                                   3
2                   3                                   0
Thus, there is no such index.



=========================================
  CODE Using PrefixSUM 
=========================================
class Solution:

  def equilibrium(self, A):
     """
    Finds the equilibrium index in an array where the sum of elements
    to the left is equal to the sum of elements to the right.

    Parameters:
    A (list[int]): List of integers.

    Returns:
    int: The index of equilibrium if found, otherwise -1.
    """

    n = len(A)    
    
    # Get in-place prefixsum
    for i in range(1, n):
      A[i] = A[i] + A[i-1]

    for i in range(n):

      if i == 0: # At index 0, prefix_sum is value at rightmost index
        left_sum = A[n-1]
      else:
        left_sum = A[i-1] # Any other index prefix_sum is  A[R] - A[L-1]

      if i == n-1:
        right_sum = 0 # At rightmost index , prefix_sum is value at 0th index
      else:
        right_sum = A[n-1] - A[i] # Any other index prefix_sum is  A[R] - A[L-1]

      if left_sum == right_sum: # if left_sum  and right_sum are same, equilibrium index is found
        return i 
      
    return -1



========================================
  CODE using python logics
=========================================

class Solution:

  def equilibrium(self, A):
     """
    Finds the equilibrium index in an array where the sum of elements
    to the left is equal to the sum of elements to the right.

    Parameters:
    A (list[int]): List of integers.

    Returns:
    int: The index of equilibrium if found, otherwise -1.
    """

    total_sum = sum(A)

    left_sum = 0

    for i in range(len(A)):

      right_sum = total_sum - left_sum - A[i] # Right sum calculation

      if left_sum == right_sum:
        return i # Found equilibrium index
            
      left_sum += A[i]

    return -1 # No equilibrium index found


'''
sol = Solution()
print(sol.equilibrium([1, 3, 5, 2, 2]))  # Output: 2 (index 2 is equilibrium)
print(sol.equilibrium([1, 2, 3]))        # Output: -1 (no equilibrium index)
print(sol.equilibrium([0, 0, 0, 0]))     # Output: 0 (index 0 is equilibrium)
print(sol.equilibrium([]))               # Output: -1 (empty array)
'''
