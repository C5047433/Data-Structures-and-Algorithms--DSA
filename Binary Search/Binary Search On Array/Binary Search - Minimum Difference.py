Problem Description
You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly built array is minimized.
The cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.
So if the newly built array is X, the element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.
Determine the minimum cost of the newly built array.


Problem Constraints
2 <= A <= 1000
2 <= B <= 1000
1 <= C[i][j] <= 10^6


Input Format
The first argument is an integer A denoting number of rows in the 2-D array.
The second argument is an integer B denoting number of columns in the 2-D array.
The third argument is a 2-D array C of size A x B.


Output Format
Return an integer denoting the minimum cost of the newly build array.


Example Input
Input 1:
 A = 2
 B = 2
 C = [ [8, 4]
      [6, 8] ]
Input 2:
 A = 3
 B = 2
 C = [ [7, 3]
       [2, 1]
       [4, 9] ]


Example Output
Output 1:
 0
Output 2:
 1


Example Explanation
Explanation 1:
 Newly build array : [8, 8]. The minimum cost will be 0 since the absolute difference will be 0(8-8).
Explanation 2:
 Newly build array : [3, 2, 4]. The minimum cost will be 1 since the minimum absolute difference will be 1(3 - 2).





CODE USING BINARY SEARCH:

class Solution:
    def BinarySearch(self,A, target):
        l = 0 
        h = len(A) -1
        while l <= h:
            mid = ( l+h) //2
            if A[mid] < target:
                l = mid+1
            elif A[mid] > target:
                h = mid -1
            else:
                return mid 
        return l if l < len(A) else h
    
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        #sor the row of matrix
        for row in C:
            row.sort()
        
        ans = float('inf')

        #iterate over last but one row with each element in next row  
        #get the index where same element or min element just less that the upper row element is present, so we get min difference   
        for i in range(A-1):
            for j in range(B):
                #iterearate over row-1 element to each element in next row to get the index of same or just less elemnt presnet in row-1
                idx = self.BinarySearch(C[i+1], C[i][j]) 
                #get the difference  and if the idx greater than
                diff = abs( C[i][j] - C[i+1][idx] )
                #if idx is greter just get difference with current elements to just previous element of idx position 
                if idx > 0:
                    diff = min(diff, C[i][j] - C[i+1][idx-1])
                #get the min difference and return it
                ans = min (diff, ans)
            
        return ans


 
        #2 pointers  --> most efficiencet menthod

        for row in C:
            row.sort()

        ans = float('inf')     
        for i in range(A-1):
            #intialize the pointer one for row-0 amd p2 for row1 and move the pinter for each row when the elemnt is min in respective row
            p1, p2=0, 0
            while p1<B and p2<B:
                diff = abs( C[i][p1] - C[i+1][p2] ) 
                ans = min(diff, ans)
                if C[i][p1] < C[i+1][p2]:
                    p1+=1
                else:
                    p2+=1
        return ans

