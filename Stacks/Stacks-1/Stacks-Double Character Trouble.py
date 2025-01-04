Problem Description
You have a string, denoted as A.

To transform the string, you should perform the following operation repeatedly:
Identify the first occurrence of consecutive identical pairs of characters within the string.
Remove this pair of identical characters from the string.
Repeat steps 1 and 2 until there are no more consecutive identical pairs of characters.
The final result will be the transformed string.

Problem Constraints
1 <= |A| <= 100000

Input Format
First and only argument is string A.

Output Format
Return the final string.

Example Input
Input 1:
 A = "abccbc"
Input 2:
 A = "ab"

Example Output
Output 1:
 "ac"
Output 2:
 "ab"

Example Explanation
Explanation 1:
The Given string is "abccbc".

Remove the first occurrence of consecutive identical pairs of characters "cc".
After removing the string will be "abbc".

Again Removing the first occurrence of consecutive identical pairs of characters "bb".
After remvoing, the string will be "ac".

Now, there is no consecutive identical pairs of characters.
Therefore the string after this operation will be "ac".

Explanation 2:
 No removals are to be done.


CODE: 

from collections import deque
class Solution:
  """
  Removes consecutive duplicate characters from a string.
  
  :param A: Input string.
  :return: Modified string with consecutive duplicates removed.
  """
  def double_char_trouble(self, A):

    stack = deque()

    for i in range(len(A)):

      #if the top element in stack, the element from the array matches, pop from stack
      if len(stack) > 0 and  stack[-1] == A[i]:
        stack.pop()
      else:
       #if it is uniqu element then push it to stack
        stack.append(A[i])

    result = []

   #build result by popping element from stack
    while len(stack) > 0 :
      result.append(stack.pop())

    return "".join(result[::-1])
      
    
