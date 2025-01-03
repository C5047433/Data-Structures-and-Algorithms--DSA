Problem Description

An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each string may be an integer or an operator.

Note: Reverse Polish Notation is equivalent to Postfix Expression, where operators are written after their operands.

Problem Constraints
1 <= N <= 10^5

Input Format
The only argument given is string array A.

Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.

Example Input
Input 1:
A =   ["2", "1", "+", "3", "*"]
Input 2:
A = ["4", "13", "5", "/", "+"]

Example Output
Output 1:
9

Output 2:
6

Example Explanation

Explaination 1:
starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9

Explaination 2:
starting from backside:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    13 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6


CODE: 

from collections import deque

class Solution:
   # @param A : list of strings
	# @return an integer
   def evalRPN(self, A):

      st = deque()

      #oterate over the array and do the necessary operation based on the expressions match else append the value to stack
      for i in range(len(A)):
         
         if A[i] in [ "+", "-", "*", "/" ]:
            #careful in picking up the fist and second value from stack, top value is always seond operand and last but second is fisrt operand
            sec_opr = st.pop()
            first_opr = st.pop()
            
            if A[i] == "+":
               st.append( first_opr + sec_opr )

            elif A[i] == "-":
               st.append( first_opr - sec_opr )

            elif A[i] == "*":
               st.append( first_opr * sec_opr ) 

            else:
               st.append( first_opr // sec_opr )
         else:
            st.append( int( A[i] ) )
   
      return st.pop() 
