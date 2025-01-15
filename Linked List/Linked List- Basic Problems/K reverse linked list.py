Problem Description
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified linked list.


Problem Constraints
1 <= |A| <= 10^3
B always divides A


Input Format
The first argument of input contains a pointer to the head of the linked list.
The second arugment of input contains the integer, B.


Output Format
Return a pointer to the head of the modified linked list.


Example Input
Input 1:
 A = [1, 2, 3, 4, 5, 6]
 B = 2
Input 2:
 A = [1, 2, 3, 4, 5, 6]
 B = 3


Example Output
Output 1:
 [2, 1, 4, 3, 6, 5]
Output 2:
 [3, 2, 1, 6, 5, 4]


Example Explanation
Explanation 1:
 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]
Explanation 2:
 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]


CODE:

class Node:
  def __init__(self, X):
    self.val = X
    self.next = None

import sys
sys.setrecursionlimit(10**6)

class Solution:
  def k_reverse(self, A, K):
    prev = None
    current = A
    nxt = None
    count = 0

    while current is not None and count < K:
      nxt = current.next
      current.next = prev
      prev = current
      current = nxt
      count += 1

    if nxt != None:
      A.next = self.k_reverse(nxt, K)

    return prev

'''
To test this code in your own environment (e.g., Google Colab or standalone script), 
uncomment(line 92 to line 130)-  the below helper functions and linked list setup code. Platforms like LeetCode 
may already provide linked list creation and testing infrastructure.

Follow these steps:
1. Uncomment the `print_list` function and the linked list setup section below.
2. Use this setup to test the `remove_duplicates` method in a local environment.
3. Ensure that the `Solution` class and `Node` class are defined before running the test code.

'''

'''
#print the updated list after reversing
def print_list(A):
  """
  Traverses and prints the linked list.

  Parameters:
  A (Node): The head of the linked list.
  """
  current = A
  while current is not None:
    print(current.val, end="->")
    current = current.next
  print("None")


#Creating Linked List input
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None


#create solution
solution = Solution()
new_head = solution.k_reverse(node1, K=5)

#print output
print_list(new_head)
'''
