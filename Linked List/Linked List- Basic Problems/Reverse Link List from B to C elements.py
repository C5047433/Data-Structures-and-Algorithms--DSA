Problem Description
Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.


Problem Constraints
1 <= |A| <= 106
1 <= B <= C <= |A|


Input Format
The first argument contains a pointer to the head of the given linked list, A.
The second arugment contains an integer, B.
The third argument contains an integer C.


Output Format
Return a pointer to the head of the modified linked list.


Example Input
Input 1:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4

Input 2:
 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5


Example Output
Output 1:
 1 -> 4 -> 3 -> 2 -> 5
Output 2:
 5 -> 4 -> 3 -> 2 -> 1


Example Explanation
Explanation 1:
 In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
 Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 
Explanation 2:
 In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
 Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 


CODE:

class Node:
  def __init__(self, X):
    self.val = X
    self.next = None

class Solution:
  def remove_nth_node_from_end(self, A, B):
    """
    Reverse element from element B to element C in the given linked list

    parameters
    :A: Head of sorted linked list
    :B: poisiton to start the reversal
    :C: position till where the revrse should be done

    :return the updated linked list
    """

    # Handle empty or single-node list
    if not A and not A.next:
      return A

    dummy = Node(0)
    dummy.next = A

    prev = dummy

    #capture the position just before the reversal start
    for i in range(B-1):
      prev = prev.next

    #store the position of start point of reversal
    start = prev.next

    current = start
    prev_rev = None

    #reverse between B and C
    for i in range(C-B+1):
      nxt = current.next
      current.next = prev_rev
      prev_rev = current
      current = nxt

    # Connect reversed segment with the rest of the list
    start.next = current  # Connect end of reversed segment
    prev.next = prev_reverse  # Connect start of reversed segment

    return dummy.next

'''
To test this code in your own environment (e.g., Google Colab or standalone script), 
uncomment(line 113 to line 154)-  the below helper functions and linked list setup code. Platforms like LeetCode 
may already provide linked list creation and testing infrastructure.

Follow these steps:
1. Uncomment the `print_list` function and the linked list setup section below.
2. Use this setup to test the `remove_duplicates` method in a local environment.
3. Ensure that the `Solution` class and `Node` class are defined before running the test code.

'''

'''
#print the updated list after deletion
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
new_head = solution.Reverse_B_to_C(node1, B=2, C=5)

#print output
print_list(new_head)
'''
