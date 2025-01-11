Problem Description
Given a sorted linked list, delete all duplicates such that each element appears only once.

Problem Constraints
0 <= length of linked list <= 106

Input Format
First argument is the head pointer of the linked list.

Output Format
Return the head pointer of the linked list after removing all duplicates.

Example Input
Input 1:
 1->1->2
Input 2:
 1->1->2->3->3

Example Output
Output 1:
 1->2
Output 2:
 1->2->3

Example Explanation
Explanation 1:
 Each element appear only once in 1->2.

CODE:
class Node:
  def __init__(self, X):
    self.val = X
    self.next = None

class Solution:
  def remove_duplicates(self, A):
    """
    Removes all the duplicates in the given linked list
    
    :A: Head of sorted linked list
    :return the updated linked list
    """
   
    #remove duplicates from Linked List
    current = A
    while current:
      #if current val and current.next.val matches, move next pointer
      while current.next and current.val == current.next.val:
        current.next = current.next.next
      current = current.next
    return A

#print the non duplicate Linked List
def print_list(A): 
    """
    Travese the updated listed list 
    
    :return the updated listed
    """   
    
    current = A
    while current:
      print(current.val, end="->")
      current = current.next
    print("None")

#Creating Linked List input
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(2)
node5 = Node(3)
node6 = Node(4)
node7 = Node(4)
node8 = Node(4)
node9 = Node(5)
node10 = Node(5)
node11 = Node(5)
node12 = Node(5)
node13 = Node(6)
node14 = Node(6)
node15 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node15
node15.next = None

#create solution
solution = Solution()
new_head = solution.remove_duplicates(node1)

#print output
print_list(new_head)


  
   


  
 
   
  


