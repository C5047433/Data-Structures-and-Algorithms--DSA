Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.


Problem Constraints
1 <= A.size() <= 10^4
1 <= A[i] <= 10^9
1 <= B <= 10^9


Input Format
First argument is an integer array A.
Second argument is an integer B.


Output Format
Return 1 if good pair exist otherwise return 0.


Example Input
Input 1:
A = [1,2,3,4]
B = 7
Input 2:
A = [1,2,4]
B = 4
Input 3:
A = [1,2,2]
B = 4


Example Output
Output 1:
1
Output 2:
0
Output 3:
1


Example Explanation
Explanation 1:
 (i,j) = (3,4)
Explanation 2:
No pair has sum equal to 4.
Explanation 3:
 (i,j) = (2,3)


===================================================
Brute Force CODE --> TC = O(N^2):
===================================================

def goodpair(A, B):

  """
  :A:  Represent an array 
  :B: Represent sum chck to be present in A

  return : 1 if pair exists else 0 
  """

  # Iterate over each elelemt in array
  for i in range(len(A)):
    # Iterate from next element till end of array 
    for j in range(i+1, len(A)):
      
      # Check if the sum of two different elements equals target_sum

      if A[i] + A[j] == B:
        return 1
  return 0

goodpair( A = [1,3,2,4], B = 7)

#output: 1



===========================================
Optimzed code for O(N) using hashmap
===========================================
def goodpair(A, B):


  """
  Check if there exists a pair of numbers in the array that sums to target_sum.
  
  :param array: List of integers.
  :param target_sum: Integer, sum to check for in the array.
  :return: 1 if such a pair exists, otherwise 0.
  """
    
  # Initialize a hashmap to store frequency of elements
  hm = {}
  
  # Capture the frequency of each element in hm as key value pair by iterrating over given array 
  for i in range(len(A)):
    
    if A[i] in hm:
      hm[A[i]] += 1
    else:
      hm[A[i]] = 1
  
  
  # Populate the hashmap with element frequencies
  for i in hm.keys():
  
    # Check if difference of element is present in hashmap 
    if B - i in hm:
  
      # If difference exists and is a duplicate (i.e., occurs twice), return 1
  
      if hm[B - i] > 1:
        return 1
  
      if B - i != i:
        return 1
  
  return 0

goodpair( A = [1,3,2,4], B = 7)
