Problem Description

Given an integer array A of size N.

If we store the sum of each triplet of the array A in a new list, then find the Bth smallest element among the list.

NOTE: A triplet consists of three elements from the array. Let's say if A[i], A[j], A[k] are the elements of the triplet then i < j < k.

Problem Constraints

3 <= N <= 500
1 <= A[i] <= 10^8
1 <= B <= (N*(N-1)*(N-2))/6

Input Format
The first argument is an integer array A.
The second argument is an integer B.

Output Format
Return an integer denoting the Bth element of the list.

Example Input

Input 1:
 A = [2, 4, 3, 2]
 B = 3

Input 2:
 A = [1, 5, 7, 3, 2]
 B = 9


Example Output
Output 1:
 9 

Output 2:
 14


Example Explanation

Explanation 1:
 All the triplets of the array A are:

 (2, 4, 3) = 9
 (2, 4, 2) = 8
 (2, 3, 2) = 7
 (4, 3, 2) = 9

 So the 3rd smallest element is 9.

CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        '''refer notes'''
        A.sort()
        n = len(A)
        l = A[0] + A[1] + A[2] #get minimun 
        h = A[n-1] + A[n-2] + A[n-3] #get max sum
        ans = -1

        while l <= h:
            mid  = ( l+h ) // 2
            tripletcount = self.Arraytripletsum(A, mid)

            if tripletcount < B:
                l = mid + 1 
            else:
                ans = mid 
                h = mid - 1
                
        
        return ans

    def Arraytripletsum(self, A, mid):
        count = 0
        n = len(A)
        
        for i in range(n-2):
            L = i + 1
            R = n - 1

            while L < R:
                triplet_sum = A[i] + A[L] + A[R]

                if triplet_sum > mid:
                    R -=1
                else:
                    count +=( R - L )
                    L +=1
                    
                
        return count
