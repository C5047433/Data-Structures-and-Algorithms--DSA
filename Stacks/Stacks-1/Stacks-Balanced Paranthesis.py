Problem Description

Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.

Problem Constraints
1 <= |A| <= 100

Input Format
The first and the only argument of input contains the string A having the parenthesis sequence.

Output Format
Return False if the parenthesis sequence is not balanced.
Return True if the parenthesis sequence is balanced.

Example Input
Input 1:
A = {([])}

Input 2:
A = (){

Input 3:
A = ()[] 

Example Output
Output 1:
 1 

Output 2:
0 

Output 3:
1 

Example Explanation
You can clearly see that the first and third case contain valid paranthesis.
In the second case, there is no closing bracket for {, thus the paranthesis sequence is invalid.rom collections import deque


from collections import deque
class Solution:
    # @param S : string
    # @return an integer
    def balanced_paranthesis(self, S):

        st = deque()

        for i in range(len(S)):

            if S[i] in [ "[", "{", "(" ]:
                st.append(S[i])

            elif S[i] == "]":
                if len(st) == 0 or st[-1] != "[":
                    return False
                st.pop()

            elif S[i] == "}":
                if len(st) == 0 or st[-1] != "{":
                    return False
                st.pop()

            else:
                if len(st) == 0 or st[-1] != "(":
                    return False
                st.pop()
            
        return len(st) == 0

