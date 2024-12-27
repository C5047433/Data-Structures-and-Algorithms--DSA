Problem Description

Given a matrix of integers A of size N x M in which each row is sorted.


Find and return the overall median of matrix A.

NOTE: No extra memory is allowed.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.



Problem Constraints

1 <= N, M <= 10^5

1 <= N*M <= 10^6

1 <= A[i] <= 10^9

N*M is odd



Input Format

The first and only argument given is the integer matrix A.



Output Format

Return the overall median of matrix A.



Example Input

Input 1:

A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 
Input 2:

A = [   [5, 17, 100]    ]


Example Output

Output 1:
 5 

Output 2:
 17



Example Explanation

Explanation 1:

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5. 
Explanation 2:

Median is 17.




Approaching Note:
Very important property : Median of an 2d Array is achieved by multiplying (len(row)*len(Col)//2)+1 


CODE:

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):
    
        n = len(A)
        m = len(A[0])
 
        required = ( (n * m)//2 + 1 )
        
        #single element array , so we get the min left value among all rows
        l = float('inf')
        for i in range(len(A)):
            l = min(l, A[i][0])

        #Max row value is at the end of each row, so among all rows what is max value
        h = float('-inf')
        for i in range(len(A)):
            h = max( A[i][-1], h ) 

        ans = -1
        
        while l <= h:
            mid = (l + h) // 2
            #use helper function for each row, get count of elements less or equal to mid and see over all elements count that are less  among matrix
            count = 0 
            for i in range(len(A)):
                 p = self.count( A[i], mid)
                 count +=p
            
            #if count is less, check if we can get more less element by travelling to left else to right
            if count >= required:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        
        return ans


    #for each row check number of elements less that the mid, so if we get the index that tell us the number of element less in the row
    def count( self, row, val ):
        l = 0 
        h = len(row)-1

        ans = -1
        
        while l <=h :
            mid = (l + h) // 2
            if row[mid] >  val: 
                h = mid -1 
            else:
                ans = mid 
                l = mid + 1

        #if we did not find any element less, then return 0 element are found 
        if ans == -1:
            return 0

        #as is 0 based index we return index+1 element are the number of elements less that the mid
        return ans+1




            


