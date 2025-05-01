Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.
Find the minimum cost to remove all elements from the array.


Problem Constraints
0 <= N <= 1000
1 <= A[i] <= 103


Input Format
First and only argument is an integer array A.


Output Format
Return an integer denoting the total cost of removing all elements from the array.


Example Input
Input 1:
 A = [2, 1]
Input 2:
 A = [5]


Example Output
Output 1:
 4
Output 2:
 5


Example Explanation
Explanation 1:
 Given array A = [2, 1]
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
 Remove 1 from the array => []. Cost of this operation is (1) = 1.
 So, total cost is = 3 + 1 = 4.
Explanation 2:
 There is only one element in the array. So, cost of removing is 5.


========================================
CODE:
========================================
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
      
    #this is van be achieved using sorting the function in reverse order
    #removing the max element , followed by second max........ and so till last least element
    #so we sort and then multiply that elemtn with (i+1) to ge tteh least sum
      A.sort(reverse = True)
      result = 0
      
      for i in range(len(A)):
        result += A[i] * (i+1)

      return result
        
