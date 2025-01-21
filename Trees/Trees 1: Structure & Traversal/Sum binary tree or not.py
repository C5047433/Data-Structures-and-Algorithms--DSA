Problem Description
Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.
An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Return 1 if it sum-binary tree else return 0.


Problem Constraints
1 <= length of the array <= 100000
0 <= node values <= 50


Input Format
The only argument given is the root node of tree A.


Output Format
Return 1 if it is sum-binary tree else return 0.


Example Input
Input 1:
       26
     /    \
    10     3
   /  \     \
  4   6      3
Input 2:
       26
     /    \
    10     3
   /  \     \
  4   6      4


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:
 All leaf nodes are considered as SumTree. 
 Value of Node 10 = 4 + 6.
 Value of Node 3 = 0 + 3 
 Value of Node 26 = (10 + 4 + 6) + 6 
Explanation 2:
 Sum of left subtree and right subtree is 27 which is not equal to the value of root node which is 26.



============================
  CODE:
============================

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:

    def solve(self, A):
        """
        Checks if the binary tree satisfies the sum binary tree property.

        :param A: TreeNode, the root of the tree
        :return: int, 1 if the tree satisfies the property, otherwise 0
        """
        self.is_valid = True
        self._check_sum_binary_tree(A)
        return 1 if self.is_valid else 0

    def _check_sum_binary_tree(self, node):
        """
        Helper function to compute the sum of the subtree and check the sum property.

        :param node: TreeNode, the current node in the traversal
        :return: int, the sum of the subtree rooted at the current node
        """
        # Base case: if the node is None, return 0
        if node is None:
            return 0

        # Compute the sum of the left and right subtrees
        left_sum = self._check_sum_binary_tree(node.left)
        right_sum = self._check_sum_binary_tree(node.right)

        # Check the sum property for non-leaf nodes
        if (node.left or node.right) and (left_sum + right_sum != node.val):
            self.is_valid = False

        # Return the sum of the current subtree
        return left_sum + right_sum + node.val

# Example Tree
#       10
#      /  \
#     4    6
#    / \
#   2   2

a = TreeNode(10)
b = a.left = TreeNode(4)
c = a.right = TreeNode(6)
d = b.left = TreeNode(2)
e = b.right = TreeNode(2)

solution = Solution()
print(solution.solve(a))  # Output: 1 (Tree satisfies sum binary tree property)
        
      
