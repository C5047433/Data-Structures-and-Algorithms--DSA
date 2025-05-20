Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.


Problem Constraints
1 <= N <= 105
A[i] ∈ ['a'-'z', 'A'-'Z']


Input Format
First and only argument is a character string A.


Output Format
Return a character string.


Example Input
Input 1:
 A = "Hello" 
Input 2:
 A = "tHiSiSaStRiNg" 


Example Output
Output 1:
 hELLO 
Output 2:
 ThIsIsAsTrInG 


Example Explanation
Explanation 1:
 'H' changes as 'h'
 'e' changes as 'E'
 'l' changesto as 'L'
 'l' changes as 'L'
 'o' changes as 'O'

Explination2:
 "tHiSiSaStRiNg" changes "ThIsIsAsTrInG".

 

 =================================
 CODE using XOR:
 =================================

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        A = list(A)
        
        for i in range(len(A)):
                A[i] = chr(ord(A[i]) ^ 32)
        return "".join(A)


======================================
CODE without XOR:
======================================
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        """
        Flips the case of each character by adjusting ASCII values.
        
        :param A: Input string
        :return: String with flipped case
        """
        
        A = list(A)
        
        for i in range(len(A)):
            if ord(A[i]) >= 97 and ord(A[i]) <= 122:
                A[i] = chr(ord(A[i]) - 32)  #lowercase to uppercase
            else:
                A[i] = chr(ord(A[i]) + 32)  #uppercase to lowercase
        return "".join(A)
