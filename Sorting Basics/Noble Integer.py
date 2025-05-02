Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.


Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108


Input Format
First and only argument is an integer array A.


Output Format
Return 1 if any such integer p is present else, return -1.


Example Input
Input 1:
 A = [3, 2, 1, 3]
Input 2:
 A = [1, 1, 3, 3]


Example Output
Output 1:
 1
Output 2:
 -1


Example Explanation
Explanation 1:
 For integer 2, there are 2 greater elements in the array..
Explanation 2:
 There exist no integer satisfying the required conditions.



========================================
   CODE:
========================================

class Solution:
    def solve(self, A):
        # Step 1: Sort the array in descending order
        A.sort(reverse=True)

        # Step 2: Edge case - if the largest number is 0,
        # then there are 0 numbers greater than it → valid Noble Integer
        if A[0] == 0:
            return 1

        current_index = 0  # This will track how many numbers are greater than the current number

        # Step 3: Iterate through the sorted array
        for i in range(1, len(A)):
            # If current element is not equal to previous, update current_index
            # current_index = count of elements before current (i.e., greater elements)
            if A[i - 1] != A[i]:
                current_index = i

            # Step 4: Check Noble Integer condition
            if A[i] == current_index:
                return 1

        # Step 5: No Noble Integer found
        return -1

s = Solution()
print(s.solve([3, 2, 1, 3]))  # Output: 1 (since 2 is a noble integer)
