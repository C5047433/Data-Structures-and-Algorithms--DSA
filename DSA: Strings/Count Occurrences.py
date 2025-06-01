Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.


Problem Constraints
1 <= |A| <= 1000


Input Format
The first and only argument contains the string A, consisting of lowercase English alphabets.


Output Format
Return an integer containing the answer.


Example Input
Input 1:
  "abobc"
Input 2:
  bobob"


Example Output
Output 1:
  1
Output 2:
  2


Example Explanation
Explanation 1:
  The only occurrence is at second position.
Explanation 2:
  Bob occures at first and third position.




======================================
CODE:
======================================

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len("bob") # Length of the pattern
        count = 0

        # Loop through the string A
        for i in range(len(A)):

             # Check if the substring from i to i + pattern_length matches the pattern
            if A[i:i+n] == "bob": 
                count += 1 # Increment the count if a match is found

        return count # Return the final count of pattern occurrences
