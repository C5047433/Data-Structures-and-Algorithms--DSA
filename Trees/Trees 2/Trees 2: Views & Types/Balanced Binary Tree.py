Problem Description
Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Problem Constraints
1 <= size of tree <= 100000


Input Format
First and only argument is the root of the tree A.


Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.


Example Input
Input 1:
    1
   / \
  2   3
Input 2:
 
       1
      /
     2
    /
   3


Example Output
Output 1:
1
Output 2:
0


Example Explanation
Explanation 1:
It is a complete binary tree.
Explanation 2:
Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
Difference = 2 > 1. 



  ===============================
  CODE:
  ===============================


  # Definition of a Binary Tree Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, A):
        """
        Checks if a binary tree is height-balanced.
        
        Args:
            A (TreeNode): The root of the binary tree.
        
        Returns:
            int: 1 if the tree is balanced, 0 otherwise.
        """
        balanced_status, _ = self.subtree_status(A)
        return int(balanced_status)

    def subtree_status(self, node):
        """
        Helper function to check balance status and height at each subtree.
        
        Args:
            node (TreeNode): The root node of the current subtree.
        
        Returns:
            tuple: (bool, int) where bool indicates if the subtree is balanced,
                   and int represents the height of the subtree.
        """
        # Base case: An empty node is balanced with a height of -1.
        if node is None:
            return True, -1

        # Get balance status and height of left subtree
        left_status, left_height = self.subtree_status(node.left)

        # Get balance status and height of right subtree
        right_status, right_height = self.subtree_status(node.right)

        # A node is balanced if:
        # - Its left and right subtrees are balanced
        # - The height difference between left and right subtrees is at most 1
        balanced_status = left_status and right_status and abs(left_height - right_height) <= 1

        # Height of the node is the max height of its left and right subtree + 1
        height = max(left_height, right_height) + 1

        return balanced_status, height
