Problem Description
Given a string A, you are asked to reverse the string and return the reversed string.


Problem Constraints
1 <= |A| <= 105
String A consist only of lowercase characters.


Input Format
First and only argument is a string A.


Output Format
Return a string denoting the reversed string.


Example Input
Input 1:
 A = "scaler"
Input 2:
 A = "academy"


Example Output
Output 1:
 "relacs"
Output 2:
 "ymedaca"


Example Explanation
Explanation 1:
 Reverse the given string.

========================================
CODE:
========================================

class Solution:
  """
  Provides a method to reverse a string using a two-pointer technique.
  """

  def solve(self, A):
      """
      Reverse the input string using in-place character swapping.

      Args:
          A: The input string to be reversed.

      Returns:
          revstr: The reversed string.
      """
      # Convert the string to a list to allow in-place modifications
      revstr = list(A)

      # Initialize two pointers: one at the start, one at the end
      i, j = 0, len(revstr) - 1

      # Swap revstr until the pointers meet in the middle
      while i < j:
          revstr[i], revstr[j] = revstr[j], revstr[i]
          i += 1  # Move the start pointer forward
          j -= 1  # Move the end pointer backward

      # Join the list back into a string and return
      return "".join(revstr)


========================================
CODE with INBUILT Function:
========================================

class Solution:
  """
  Provides a method to reverse a string using a two-pointer technique.
  """

  def solve(self, A):
   return A[::-1]
