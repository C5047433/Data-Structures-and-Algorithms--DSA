Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
and at least one occurrence of the minimum value of the array.


Problem Constraints
1 <= |A| <= 2000


Input Format
First and only argument is vector A


Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array


Example Input
Input 1:
A = [1, 3, 2]
Input 2:
A = [2, 6, 1, 6, 9]


Example Output
Output 1:
 2
Output 2:
 3


Example Explanation
Explanation 1:
 Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
Explanation 2:
 Take the last 3 elements of the array.



===================================================
  CODE:
===================================================


class Solution:

  """
  Finds the smallest contiguous subarray containing both 
  the minimum and maximum elements in the list.
  """

  def solve(self, A):
      """
      :param A: List[int] - List of integers
      :return: int - Length of the smallest subarray containing both min and max elements
      """
      min_val = min(A)  # Get minimum value in the array
      max_val = max(A)  # Get maximum value in the array

      last_min = -1 #intialize the min value occurance subarray value as -1
      last_max = -1 #intialize the max value occurance subarray value as -1

      result = len(A)

      if mn == mx:  #Edge Cae: Single element array or array of same elements
        return 1

      for i in range(len(A)):
        
        if A[i] == mn: # If element matches mn, assign the index position to last_min
          last_min = i

          if last_max != -1: # if last_max found, get the lenght of array size where both min and max are present
            result = min(result, last_min - last_max + 1 )

        elif A[i] == mx: # If element matches mx, assign the index position to last_max
          last_max = i

          if last_min != -1: # if last_min found, get the lenght of array size where both min and max are present
            result = min(result, last_max - last_min + 1 )
        
      return result 

      
