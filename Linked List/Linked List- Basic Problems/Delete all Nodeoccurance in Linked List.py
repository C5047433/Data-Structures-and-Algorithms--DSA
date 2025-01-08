Given a singly linked list and a value x, write a function to delete all occurrences of x in the linked list.
The function should return the head of the modified linked list after removing all nodes with the value x.

Problem Constraints:
The linked list can have 0 ≤ n ≤ 10⁵ nodes, where n is the number of nodes in the list.
The value of each node in the linked list and the value of x satisfy -10⁵ ≤ Node.data, x ≤ 10⁵.
The function should handle edge cases such as:
An empty linked list.
A linked list with all nodes having the value x.
A linked list where no nodes have the value x.


Input:
The linked list is represented using a series of Node objects, where each Node contains:
data: An integer value.

next: A reference to the next node in the list (or None if it is the last node).
An integer x representing the value to be deleted from the linked list.
Output:
Return the head of the modified linked list after deleting all nodes with the value x.
Example:
Example 1:

Input:
Linked List: 1 -> 2 -> 3 -> 4 -> 2 -> 5
x = 2

Output:
1 -> 3 -> 4 -> 5

Explanation:
All occurrences of 2 are removed from the linked list.

Example 2:

Input:
Linked List: 2 -> 2 -> 2
x = 2

Output:
None (or an empty linked list)

Explanation:
All occurrences of 2 are removed, leaving an empty list.

Problem Constraints:
The linked list can have 0 ≤ n ≤ 10⁵ nodes, where n is the number of nodes in the list.
The value of each node in the linked list and the value of x satisfy -10⁵ ≤ Node.data, x ≤ 10⁵.
The function should handle edge cases such as:
An empty linked list.
A linked list with all nodes having the value x.
A linked list where no nodes have the value x.



CODE:

class Node:
    def __init__(self, X):
        self.val = X
        self.next = None

class Solution:
    def ele_deletion(self, A, k):
        """
        Deletes all occurrences of the value `k` in the linked list.

        :param A: Head of the linked list.
        :param k: Value to be deleted.
        :return: New head of the modified linked list.
        """
        # Handle cases where the head contains the value `k`
        while A is not None and A.val == k:
            A = A.next

        # Traverse the list to remove nodes with value `k`
        current = A
        while current is not None and current.next is not None:
            if current.next.val == k:
                current.next = current.next.next
            else:
                current = current.next

        return A  # Return the new head of the list

def print_list(head):
    """
    Prints the linked list from the given head node.
    """
    temp = head
    while temp is not None:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

# Example Usage
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(7)
node5 = Node(10)
node6 = Node(4)
node7 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

solution = Solution()
new_head = solution.ele_deletion(node1, k=7)

# Print the modified list
print_list(new_head)

