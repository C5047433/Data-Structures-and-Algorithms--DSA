Problem Description
Given an array A of N integers. 
Count the number of elements that have at least 1 elements greater than itself.


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9


Input Format
First and only argument is an array of integers A.


Output Format
Return the count of elements.


Example Input
Input 1:
A = [3, 1, 2]
Input 2:
A = [5, 5, 3]


Example Output
Output 1:
2
Output 2:
1


Example Explanation
Explanation 1:
The elements that have at least 1 element greater than itself are 1 and 2
Explanation 2:
The elements that have at least 1 element greater than itself is 3



============================================
CODE:
============================================

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

      # Find the maximum element in array
      mx = A[0]
  
      for i in A:
        if mx < i:
          mx = i
    
      # Find count of occurance of mx in A  
      count = 0  

      for i in A:
        if i == mx:
          count += 1
          
      # return count of elements less than the max element
      return len(A) - count


        '''
        #simple code
        mx = max(A)
        count = A.count(mx)
        return len(A) - count

        '''

