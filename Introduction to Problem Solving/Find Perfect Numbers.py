Problem Description
You are given an integer A. You have to tell whether it is a perfect number or not.
Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
A proper divisor of a natural number is the divisor that is strictly less than the number.


Problem Constraints
1 <= A <= 106


Input Format
First and only argument contains a single positive integer A.


Output Format
Return 1 if A is a perfect number and 0 otherwise.


Example Input
Input 1:
A = 4
Input 2:
A = 6


Example Output
Output 1:
0 
Output 2:
1 


Example Explanation
Explanation 1:
For A = 4, the sum of its proper divisors = 1 + 2 = 3, is not equal to 4.
Explanation 2:
For A = 6, the sum of its proper divisors = 1 + 2 + 3 = 6, is equal to 6. 

===================================
CODE:
===================================

class Solution:

    def perfect_numbers(self, A):
      """
      :param A : integer
      :return: 1 if A is a perfect number, otherwise 0
      """
      if A < 2:
            return 0  # Perfect numbers are greater than 1

      i = 1 #intialize divisors
      result = 0 #intialize sum 

      #iterate over all divisors less than A
      while i < A:

        #check all the divisors and apend to result
        if A % i == 0:
          result += i

        i += 1 #increment i

      #return 1 if sum of all divisors is equal to A else 0
      return 1 if result == A else 0

solution = Solution()
print(solution.perfect_numbers(A=9))

