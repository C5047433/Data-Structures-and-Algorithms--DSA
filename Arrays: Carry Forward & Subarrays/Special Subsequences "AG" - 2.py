
Problem Description
You have given a string A having Uppercase English letters.
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.


Problem Constraints
1 <= length(A) <= 10^5


Input Format
First and only argument is a string A.


Output Format
Return an long integer denoting the answer.


Example Input
Input 1:
 A = "ABCGAG"
Input 2:
 A = "GAB"


Example Output
Output 1:
 3
Output 2:
 0


Example Explanation
Explanation 1:
 Subsequence "AG" is 3 times in given string, the pairs are (0, 3), (0, 5) and (4, 5). 
Explanation 2:
 There is no subsequence "AG" in the given string.


=======================================
  CODE using python style:
=======================================

class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):
        a_g_pairs = 0
        a_count = 0
      
        for i in A:
            if i == "A":      
                a_count += 1

            #for every G, append the count of "a" so those many comnonations of "AG" pairs can be formed
            elif i == "G":
                a_g_pairs += a_count
              
        #finally once all the pairs are calucalted return the count of pairs
        return a_g_pairs




==========================================
Code Using prefixSum menthod:
==========================================

class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):

     psum = [0] * len(A)
     if A[0] == "A":
        psum[0] = 1

     for i in range(1, len(A)):
        if A[i] == "A":
           psum[i] = 1 + psum[i-1]
        else:
           psum[i] = psum[i-1]

     count_a_g = 0
     for i in range(1, len(A)):
        if A[i] == "G":
           count_a_g += psum[i-1]
     return count_a_g
            
