Problem Description
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

Problem Constraints
1 <= |A| <= 10^5
0 <= A[i] <= 10^9


Input Format
The first argument is an integer array A.


Output Format
Return the second largest element. If no such element exist then return -1.


Example Input
Input 1:
 A = [2, 1, 2] 
Input 2:
 A = [2]


Example Output
Output 1:
 1 
Output 2:
 -1 


Example Explanation
Explanation 1:
 First largest element = 2
 Second largest element = 1
Explanation 2:
 There is no second largest element in the array.



===============================================
  CODE:
===============================================

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        """
        Returns the second maximum element in the given list.
            
        If all elements are the same or there's only one element, returns None.
        """

        # Edge Case: single element array
        if len(A) < 2:
            return -1
        
        # Find max element in the array
        max_element = A[0]

        for i in range(1, len(A)):
            
            if max_element < A[i]:
                max_element = A[i]

        second_max = -1
        # Second max element is greater than all element and less than first max element 
        for i in A:
            
            if i < max_element and i > second_max:
                second_max = i
            
        return second_max
    

          

