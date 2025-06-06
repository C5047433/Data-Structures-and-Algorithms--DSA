Problem Description
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
NOTE: 'a' , 'e , 'i' , 'o' , 'u' are defined as vowels.


Problem Constraints
1<=N<=100000


Input Format
First argument is a string A of size N.


Output Format
Return the resultant string.


Example Input
Input 1:
A="aeiOUz"
Input 2:
A="AbcaZeoB"


Example Output
Output 1:
"###z###z"
Output 2:
"bc###bc###"


Example Explanation
Explanatino 1:
First concatenate the string with itself so string A becomes "aeiOUzaeiOUz".
Delete all the uppercase letters so string A becomes "aeizaeiz".
Now replace vowel with '#', A becomes "###z###z".
Explanatino 2:
First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
Delete all the uppercase letters so string A becomes "bcaeobcaeo".
Now replace vowel with '#', A becomes "bc###bc###".



=======================================
CODE:
========================================
class Solution:
    """A class that provides string manipulation methods."""

    def solve(self, A):
        """
        Processes the input string by duplicating it, extracting lowercase letters,
        replacing vowels with '#', and returning the modified string.

        Args:
            A (str): The input string to process.

        Returns:
            str: The processed string with vowels replaced by '#'.
        """
        
        A = A + A
        newlist = list(A)
        B = []

        for i in newlist:
          if i.islower():
            B.append(i)

        vowels = "aeiou"

        for i in range(len(B)):
          if B[i] in vowels:
            B[i] = '#'

        return "".join(B)

            
