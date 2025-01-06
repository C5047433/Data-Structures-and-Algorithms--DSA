Problem Description

You are given a linked list A
Each node in the linked list contains two pointers: a next pointer and a random pointer
The next pointer points to the next node in the list
The random pointer can point to any node in the list, or it can be NULL
Your task is to create a deep copy of the linked list A
The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
You should create a new linked list B, where each node in B has the same value as the corresponding node in A
The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)

Problem Constraints
0 <= |A| <= 10^6

Input Format
The first argument of input contains a pointer to the head of linked list A.

Output Format
Return a pointer to the head of the required linked list.

Example Input
Given list
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  
Example Output
   1 -> 2 -> 3
with random pointers going from
  1 -> 3
  2 -> 1
  3 -> 1
  


Example Explanation
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.



CODE:

class RandomListNode():
    def __init__(self, X):
        self.label = X
        self.next = None
        Self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

    def copyRandomList(self, head):
        
        #Step1: Create Copy of Linked List
        temp = head

        while temp is not None:
            nxt = temp .next
            temp.next = RandomListNode(temp.label)
            temp.next.next = nxt

            temp = temp.next.next

        
        #Step2: copy random Pointer

        temp = head

        while temp is not None:
            if temp.random is not None:
                temp.next.random = temp.random.next

            temp = temp.next.next

        
        #step3: sepearate origin and New list
        
        temp = head
        head2 = temp.next
        temp2 = head2

        while temp is not None:
            temp.next = temp.next.next

            if temp2.next is not None:
                temp2.next = temp2.next.next

            temp = temp.next 
            temp2 = temp2.next

        return head2

         
        '''
        Update below line incase if you are woking on you own compiler like google colab or any other to test and print inputs
        
        comment last line94 from above code and uncomment below lines(line 97 -line 132): 
        #return = head2

        temp = head2

        while temp is not None:
          print("val", temp.label, "random", temp.random.label)
          print()
          temp = temp.next
        return head2


node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node4 = RandomListNode(4)
node5 = RandomListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = node5
node2.random = node4
node3.random = node1
node4.random = node3
node5.random = node2


solution = Solution()
new_head = solution.copyRandomList(node1)
        '''        





