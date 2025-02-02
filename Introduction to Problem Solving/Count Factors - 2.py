Problem Description
Given an integer A, you need to find the count of it's factors.

Factor of a number is the number which divides it perfectly leaving no remainder.

Example : 1, 2, 3, 6 are factors of 6


Problem Constraints
1 <= A <= 10^9


Input Format
First and only argument is an integer A.


Output Format
Return the count of factors of A.


Example Input
Input 1:
5
Input 2:
10


Example Output
Output 1:
2
Output 2:
4


Example Explanation
Explanation 1:
Factors of 5 are 1 and 5.
Explanation 2:
Factors of 10 are 1, 2, 5 and 10.


========================
CODE:
========================

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i=1
        count=0
        #iterate over loop untill you get the square root of a number, as this will help us to achieve the other values which are repative 
        #automatically
        while i*i<=A:
            #if the nuber completely divides then it mean that number is its factor, so count that number
            if A%i == 0: 
                count+=1
                #if by ancy change is the i and A% i is same then just the are same nuber and we need to conunt only once
                if i != A//i:
                    count+=1
                    #keep incresing the value of is by 1
            i+=1
        return count
