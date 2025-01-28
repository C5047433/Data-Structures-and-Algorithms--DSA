Problem Description
Given the inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.


Problem Constraints
1 <= number of nodes <= 10^5


Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.


Output Format
Return the root node of the binary tree.


Example Input
Input 1:
 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:
 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


Example Output
Output 1:
   1
  / \
 2   3
Output 2:
   1  
  / \
 6   2
    /
   3


Example Explanation
Explanation 1:
 Create the binary tree and return the root node of the tree.



=============================
CODE:
=============================

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTreeConstructor:
    def construct_tree_from_inorder_postorder(self, inorder, postorder):
        """
        Constructs a binary tree from the given inorder and postorder traversal arrays.
        :param inorder: List[int] - The inorder traversal of the tree.
        :param postorder: List[int] - The postorder traversal of the tree.
        :return: TreeNode - Root of the constructed binary tree.
        """
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None

        return self.tree_from_inord_postord(
            inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1
        )

    def tree_from_inord_postord(self, inorder, postorder, i1, j1, i2, j2):
        """
        Helper function to recursively construct the binary tree.
        :param inorder: List[int] - The inorder traversal of the tree.
        :param postorder: List[int] - The postorder traversal of the tree.
        :param i1: int - Start index of the current inorder segment.
        :param j1: int - End index of the current inorder segment.
        :param i2: int - Start index of the current postorder segment.
        :param j2: int - End index of the current postorder segment.
        :return: TreeNode - Root of the constructed binary tree for this segment.
        """
        if i1 > j1:
            return None

        # The last element of the current postorder segment is the root.
        root_value = postorder[j2]
        root = TreeNode(root_value)

        # Find the index of root_value in the inorder array.
        idx = inorder.index(root_value, i1, j1 + 1)

        # Calculate the size of the left subtree.
        left_subtree_size = idx - i1

        # Recursively construct the left and right subtrees.
        root.left = self.tree_from_inord_postord(
            inorder, postorder, i1, idx - 1, i2, i2 + left_subtree_size - 1
        )
        root.right = self.tree_from_inord_postord(
            inorder, postorder, idx + 1, j1, i2 + left_subtree_size, j2 - 1
        )

        return root




