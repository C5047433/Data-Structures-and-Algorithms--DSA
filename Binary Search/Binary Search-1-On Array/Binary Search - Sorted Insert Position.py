Problem Description
You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
If the target value is not found and least number greater than equal to target is also not present, return the length of array (i.e. the position where target can be placed)
Your solution should have a time complexity of O(log(N)).


Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^5
1 <= B <= 10^5


Input Format
The first argument is an integer array A of size N.
The second argument is an integer B.


Output Format
Return an integer denoting the index of target value.


Example Input
Input 1:
A = [1, 3, 5, 6]
B = 5 
Input 2:
A = [1, 4, 9]
B = 3


Example Output
Output 1:
2 
Output 2:
1


Example Explanation
Explanation 1:
The target value is present at index 2. 
Explanation 2:
The target value should be inserted at index 1.


CODE:

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        l=0
        h=len(A)-1
        ans=-1
        # If the target value is present, return its index.
        while l<=h:
            mid=(l+h)//2
            if A[mid]<B:
                l=mid+1
            elif A[mid]>B:
                h=mid-1
            else:
                ans=mid
                return ans 

        if ans == -1 and l > len(A):
            return len(A)
        return l
        
        '''

        'below code might take O(N) TC in worst case so replaces with aobove last three lines '    

        '''        
        #If the target value is not found, return the index of least element greater than equal to B. search range is (ans+1,len(A))
        if ans==-1:
            for i in range(ans+1,len(A)):
                if A[i]>A[ans]:
                    return i
        #If the target value is not found, least no >= to target is also not present, return the length of array (i.e. the position where target can be placed)
        if ans==-1:
            for i in range(len(A)):
                if A[i]>B:
                    return i
        #none of the above conditions satisfy then element can be added at the end of array so return len(A)
        return len(A)
        '''





            


