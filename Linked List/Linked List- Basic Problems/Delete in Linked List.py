Problem Description
You are given the head of a linked list A and an integer B. Delete the B-th node from the linked list.
Note : Follow 0-based indexing for the node numbering.

Problem Constraints
1 <= size of linked list <= 10^5
1 <= value of nodes <= 10^9
0 <= B < size of linked list

Input Format
The first argument A is the head of a linked list.
The second arguement B is an integer.

Output Format
Return the head of the linked list after deletion

Example Input
Input 1:
A = 1 -> 2 -> 3
B = 1

Input 2:
A = 4 -> 3 -> 2 -> 1
B = 0

Example Output
Output 1:
1 -> 3

Output 2:
3 -> 2 -> 1

Example Explanation
For Input 1:
The linked list after deletion is 1 -> 3.
For Input 2:
The linked list after deletion is 3 -> 2 -> 1.


CODE:
class Node:
  def __init__(self, X):
    self.val = X
    self.next = None

class Solution:
  def Delete_in_LinkedList(self, A, k):

    temp = A
    for i in range(p-1):
      temp = temp.next
    temp.next = temp.next.next
    
    temp = A
    for i in range(p):
      temp = temp.next
    return temp.val

    return A
    
    '''
    Update below line incase if you are woking on you own compiler like google colab or any other to test and print inputs
    
    comment last line - 59 from above code and uncomment below lines(line 67 -line 90): 
    #return A

    temp = A
    while temp != None:
      print(temp.val, end=",")
      temp = temp.next

node1 = Node(1)
node2 = Node(2)
node3= Node(3)
node4= Node(7)
node5= Node(10)
node6 = Node(4)
node7 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None


solution = Solution()

new_head = solution.ele_deletion(node1, k=7 )
'''

        
