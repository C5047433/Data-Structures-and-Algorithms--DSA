Problem Description
Given a linked list A, remove the B-th node from the end of the list and return its head.
For example, given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.


Problem Constraints
1 <= |A| <= 10^6


Input Format
The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.


Output Format
Return the head of the linked list after deleting the B-th element from the end.


Example Input
Input 1:
A = 1->2->3->4->5
B = 2
Input 2:
A = 1
B = 1


Example Output
Output 1:
1->2->3->5
Output 2:
  


Example Explanation
Explanation 1:
In the first example, 4 is the second last element.
Explanation 2:
In the second example, 1 is the first and the last element.


CODE:

class Node:
  def __init__(self, X):
    self.val = X
    self.next = None

class Solution:
  def remove_nth_node_from_end(self, A, B):
    """
    Removes nth node from end in the given linked list
    
    parameters
    :A: Head of sorted linked list
    :B: poisiton to delete from the end

    :return the updated linked list
    """
    
    #caluclate the length of linked list
    length = 0
    current = A
    while current is not None:
      length += 1
      current = current.next
  

    #delete at unknown position delete at the start of the Linked list
    current = A
    if B >= length:
      return current.next
    
    else:
      #delete at the required position
      position = length - B
      #print("position", position)
      for i in range(position-1):
        current = current.next 
      current.next = current.next.next
    return A


'''
To test this code in your own environment (e.g., Google Colab or standalone script), 
uncomment(line 100 to line 140)-  the below helper functions and linked list setup code. Platforms like LeetCode 
may already provide linked list creation and testing infrastructure.

Follow these steps:
1. Uncomment the `print_list` function and the linked list setup section below.
2. Use this setup to test the `remove_duplicates` method in a local environment.
3. Ensure that the `Solution` class and `Node` class are defined before running the test code.

'''

'''
# Helper function to print the updated linked list after deletion
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
new_head = solution.remove_nth_node_from_end(node1, B=1)

#print output
print_list(new_head)

  
