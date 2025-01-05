Problem Description
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
Check whether A has redundant braces or not.
NOTE: A will be always a valid expression and will not contain any white spaces.

Problem Constraints
1 <= |A| <= 105

Input Format
The only argument given is string A.

Output Format
Return 1 if A has redundant braces else, return 0.

Example Input
Input 1:
A = "((a+b))"

Input 2:
A = "(a+(a+b))"

Example Output
Output 1:
True

Output 2:
False

Example Explanation
Explanation 1:
 ((a+b)) has redundant braces so answer will be 1.
Explanation 2:
 (a+(a+b)) doesn't have have any redundant braces so answer will be 0.


CODE: 

from collections import deque
class Solution:
  def braces(self, A):
  
    # Evaluate if the expression contains redundant braces.

    # param A: str - Input string representing the expression.
    # return: bool - True if redundant braces are found, False otherwise.
    

    A = list(A)
    stack = deque()
    #intialize that there is no redundant expression 
    redundant = False
    
    for i in range(len(A)):
      #Between brackets if there are any arthematic operator then it is not redundant 
      if A[i] == ")":
        #if there is bracket set redundant = True
        redundant = True

        #pop out all the values between the brackets and check if there exists an arthmatic opeator and set redundant = False
        while len(stack) > 0 and  stack[-1] != "(":
          if stack[-1] in ["+", "-", "*", "/"]:
            redundant = False
          stack.pop()

        #after poping if the value is redundant = True , jsut return the result
        if redundant:
          return redundant

      #after poping , if there is pair of braces i.e () , then pop
      if A[i] == ")" and stack[-1] == "(":
          stack.pop()

      #append the open brace and set the redundant = True
      elif A[i] == "(":
        stack.append(A[i])
        redundant = True

      #append all the other char as we travese
      else:
        stack.append(A[i])

  return redundant
