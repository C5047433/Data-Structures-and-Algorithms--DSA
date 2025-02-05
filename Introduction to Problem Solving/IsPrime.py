Problem Description
Given a number A. Return 1 if A is prime and return 0 if not. 

Note : 
The value of A can cross the range of Integer.


Problem Constraints
1 <= A <= 10^9


Input Format
The first argument is a single integer A.


Output Format
Return 1 if A is prime else return 0.


Example Input
Input 1:
A = 5
Input 2:
A = 10


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
5 is a prime number.
Explanation 2:
10 is not a prime number.

=============================
CODE:
=============================
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        #1 is not a prime number so we intialize from 2
        i=1
        count = 0
      
        #we iterate till the squareroot of A
        while i * i <= A:
            #check if the nuber is divisible by i or not, if yes increase the count by 1
            if A%i == 0:
                count += 1
                
                if i != A // i: # If it's a distinct factor, count it separately
                    count += 1
                     
            i += 1 #keep increasing the value of i
        
        # A prime number has exactly 2 factors (1 and itself)
        return 1 if count == 2 else 0
