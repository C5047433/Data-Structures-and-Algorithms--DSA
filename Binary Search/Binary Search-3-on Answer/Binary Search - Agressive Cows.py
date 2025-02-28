Problem Description

Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.

Output Format
Return the largest minimum distance possible among the cows.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 3

Input 2:
A = [1, 2]
B = 2

Example Output
Output 1:
 2

Output 2:
 1

Example Explanation
Explanation 1:
 John can assign the stalls at location 1, 3 and 5 to the 3 cows respectively. So the minimum distance will be 2.

Explanation 2:
The minimum distance will be 1.


CODE:

# @param A : integer
# @param B : integer
# @param C : list of integers
# @return an integer

def agressiveCows(A, B):
    A.sort() #sort the stalls
    n = len(A)
    l = 1
    h = A[n-1] - A[0]

    while l <= h:
        mid = ( l + h ) //2 

        if count_of_cows(A, mid, n) >= B:
            l = mid + 1 
            ans = mid 
        else:
            h = mid - 1

    return ans

def count_of_cows( A, mid, n):
    count = 1 
    position = A[0]  #first placement of cow
    #distance is greaterthan mid, we can place a cow, start fresh at the position to see next placement of cow
    for i in range(1, n):
        if A[i] - position >= mid:
            count +=1
            position = A[i]

    return count

