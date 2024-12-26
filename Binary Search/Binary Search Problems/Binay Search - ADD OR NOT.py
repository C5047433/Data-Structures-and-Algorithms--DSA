Problem Description

Given an array of integers A of size N and an integer B.

In a single operation, any one element of the array can be increased by 1. You are allowed to do at most B such operations.

Find the number with the maximum number of occurrences and return an array C of size 2, where C[0] is the number of occurrences, and C[1] is the number with maximum occurrence.
If there are several such numbers, your task is to find the minimum one.

Problem Constraints
1 <= N <= 10**5

-10**9 <= A[i] <= 10**9

0 <= B <= 10**9

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return an array C of size 2, where C[0] is number of occurence and C[1] is the number with maximum occurence.

Example Input
Input 1:
 A = [3, 1, 2, 2, 1]
 B = 3

Input 2:
 A = [5, 5, 5]
 B = 3

Example Output
Output 1:
 [4, 2]

Output 2:
 [3, 5]

Example Explanation
Explanation 1:
 Apply operations on A[2] and A[4]
 A = [3, 2, 2, 2, 2]
 Maximum occurence =  4
 Minimum value of element with maximum occurence = 2

Explanation 2:
 A = [5, 5, 5]
 Maximum occurence =  3
 Minimum value of element with maximum occurence = 5


CODE:
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # Step 1: Sort the array
        A.sort()
        n = len(A)
        
        # Variables for sliding window and result
        left = 0
        current_sum = 0
        max_frequency = 0
        best_number = 0

        # Step 2: Sliding window
        for right in range(n):
            current_sum += A[right]   # Add the current element to the window sum

            # Calculate the operations required for the current window
            window_size = right - left + 1
            required_operations = A[right] * window_size - current_sum
           
            # If operations exceed B, shrink the window
            while required_operations > B:
                current_sum -= A[left]
                left += 1
                window_size = right - left + 1
                required_operations = A[right] * window_size - current_sum
                
            # Update maximum frequency and best number
            if window_size > max_frequency:
                max_frequency = window_size
                best_number = A[right]
               
        # Step 3: Return the result
        return [max_frequency, best_number]