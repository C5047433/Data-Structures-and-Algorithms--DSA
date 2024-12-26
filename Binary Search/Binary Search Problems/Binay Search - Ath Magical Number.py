Problem Description

You are given three positive integers, A, B, and C.

Any positive integer is magical if divisible by either B or C.

Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.

Note: Ensure to prevent integer overflow while calculating.



Problem Constraints

1 <= A <= 10^9

2 <= B, C <= 40000



Input Format

The first argument given is an integer A.

The second argument given is an integer B.

The third argument given is an integer C.



Output Format

Return the Ath smallest magical number. Since the answer may be very large, return modulo 109 + 7.



Example Input

Input 1:

 A = 1
 B = 2
 C = 3
Input 2:

 A = 4
 B = 2
 C = 3


Example Output

Output 1:

 2
Output 2:

 6


Example Explanation

Explanation 1:

 1st magical number is 2.
Explanation 2:

 First four magical numbers are 2, 3, 4, 6 so the 4th magical number is 6.

Note/Hint to Code:
Numbers divisible by B and C in a range of [1,M] is given by M/B + M/C - M/lcm(B,C)


CODE:
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        l = 1
        h = min(B, C) * A 

        while l <= h:
            mid = ( l + h ) // 2
            count = self.findcount(mid, B, C)

            if count < A:
                l = mid + 1
            else:
                h = mid - 1
        return l % ( (10**9) + 7 ) 
        
    def gcd(self, B, C):
        if C == 0:
            return B
        return self.gcd(C, B % C)

    def lcm(self,B,C):
        LCM = (B * C) // self.gcd(B, C)
        return LCM

    def findcount(self, mid, B, C):
        count = ( mid//B ) + ( mid//C ) - ( mid//self.lcm(B, C) )
        return count



        

