Problem Description
You are given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.


Problem Constraints
1 <= N <= 3 * 10^5


Input Format
The only argument given is string A.


Output Format
Return the string A after reversing the string word by word.


Example Input
Input 1:
A = "the sky is blue"
Input 2:
A = "this is ib"


Example Output
Output 1:
"blue is sky the"
Output 2:
"ib is this"    


Example Explanation
Explanation 1:
We reverse the string word by word so the string becomes "blue is sky the".
Explanation 2:
We reverse the string word by word so the string becomes "ib is this".



====================================
  CODE without INBUILT function:
====================================

class Solution:
    """
    Provides a method to reverse the order of words in a sentence.
    """

    def solve(self, A):
        """
        Reverse the sequence of words in the input string.

        Args:
            text (A): A sentence consisting of words separated by spaces.

        Returns:
            A: A string with word order reversed.
        """
        # Split the sentence into words
        words = text.split()

        # Initialize two pointers at the start and end of the list
        i, j = 0, len(words) - 1

        # Swap words until pointers meet
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        # Rejoin the words into a single string
        return " ".join(words)



====================================
  CODE with INBUILT function:
====================================

class Solution:
    """
    Provides a method to reverse the order of words in a sentence.
    """
    def solve(self, A):
        A = A.split()
        return " ".join(A[::-1])
