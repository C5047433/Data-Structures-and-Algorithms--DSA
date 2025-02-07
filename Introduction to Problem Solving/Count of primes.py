Problem Description
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.


Problem Constraints
0 <= n <= 10^3


Input Format
Single input parameter n in function.


Output Format
Return the count of prime numbers less than or equal to n.


Example Input
Input 1:
19
Input 2:
1


Example Output
Output 1:
8
Output 2:
0


Example Explanation
Explanation 1:
Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
Explanation 2:
There are no primes <= 1

=================================
CODE:
=================================


class Solution:
    
    def solve(self, A):
      
    """
    # @param A : integer
    # @return an integer
    """
      count = 0
        
      for j in range(2, A+1):
          if self.checkprime(j):
              count+=1
      return count
    
    def checkprime(self, N):
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
            i+=1
        return i>=2

   
