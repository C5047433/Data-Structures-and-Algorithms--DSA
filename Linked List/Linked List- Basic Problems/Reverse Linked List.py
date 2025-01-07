Problem Description
You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.
NOTE: You have to do it in-place and in one-pass.

Problem Constraints
1 <= Length of linked list <= 105
Value of each node is within the range of a 32-bit integer.

Input Format
First and only argument is a linked-list node A.

Output Format
Return a linked-list node denoting the head of the reversed linked list.

Example Input
Input 1:
 A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 

Input 2:
 A = 3 -> NULL 

Example Output
Output 1:
 5 -> 4 -> 3 -> 2 -> 1 -> NULL 

Output 2:
 3 -> NULL 


Example Explanation
Explanation 1:
 The linked list has 5 nodes. After reversing them, the list becomes : 5 -> 4 -> 3 -> 2 -> 1 -> NULL 

Expalantion 2:
 The linked list consists of only a single node. After reversing it, the list becomes : 3 -> NULL 


CODE:

class ListNode:
  def __init__(self, X):
    self.val = X
    self.next= None

class Solution:
  def reverse_linkedlist(self, A):
    current = A
    prev = None

    while current is not None:
      nxt = current.next
      current.next = prev
      prev = current
      current = nxt
    
    return prev

    '''
    Update below line incase if you are woking on you own compiler like google colab or any other to test and print outputs
        
    comment last line57 from above code and uncomment lines64 - line87: 
    #return prev
    temp = prev
    while temp != None:
      print(temp.val)
      temp = temp.next
  
  
node1 = Node(1)
node2 = Node(2)
node3= Node(3)
node4= Node(4)
node5= Node(5)
node6= Node(6)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None

solution = Solution()
new_head = solution.reverse_linkedlist(node1)
'''


    
