Problem Description
You are given A which is the head of a linked list. Also given is the value B and position C. Complete the function that should insert a new node with the said value at the given position.
Notes:
In case the position is more than length of linked list, simply insert the new node at the tail only.
In case the pos is 0, simply insert the new node at head only.
Follow 0-based indexing for the node numbering.

Problem Constraints
0 <= size of linked list <= 10^5
1 <= value of nodes <= 10^9
1 <= B <= 10^9
0 <= C <= 10^5

Input Format
The first argument A is the head of a linked list.
The second argument B is an integer which denotes the value of the new node
The third argument C is an integer which denotes the position of the new node

Output Format
Return the head of the linked list

Example Input
Input 1:
A = 1 -> 2
B = 3
C = 0
Input 2:
A = 1 -> 2
B = 3
C = 1

Example Output
Output 1:
3 -> 1 -> 2
Output 2:
1 -> 3 -> 2

Example Explanation
For Input 1:
The new node is add to the head of the linked list
For Input 2:
The new node is added after the first node of the linked list


CODE:

class ListNode:
  def __init__(self, X):
    self.val = X
    self.next = None
  
class Solution:
  def insert_linkedlist(self, A, B, C):
    temp = A

    #if A is None return B
    if A is None:
      return ListNode(B)

    #Inesrt at the head
    if C == 0:
      newNode = ListNode(B)
      newNode.next = A
      return newNode

    '''Note: THis is useful only to print after appending at the head
     temp = newNode
     while temp is not None:
       print(temp.val)
       temp = temp.next
    '''

    #inert at the tail
    temp = A
    count = 0
    while temp is not None:
      count += 1
      temp = temp.next

    if C > count:
      temp = A
      while temp.next is not None:
        temp = temp.next
      newNode = ListNode(B)
      temp.next = newNode
      newNode.next = None
      return A
    else:
      temp = A
      for i in range(C-1):
          temp = temp.next
  
      newNode = ListNode(B)
      newNode.next = temp.next
      temp.next = newNode
  
    return A

    #print update the list after inserting at index C
    temp = A
    while temp is not None:
      print(temp.val, end="-->")
      temp = temp.next


node1 = ListNode(1)
node2 = ListNode(2)
node3= ListNode(3)
node4= ListNode(7)
node5= ListNode(10)
node6= ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

solution = Solution()

print(solution.insert_linkedlist(node1, B=11, C=7))

