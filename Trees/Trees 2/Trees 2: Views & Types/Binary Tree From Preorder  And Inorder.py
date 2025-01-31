Problem Description
Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.


Problem Constraints
1 <= number of nodes <= 10^5


Input Format
First argument is an integer array A denoting the preorder traversal of the tree.
Second argument is an integer array B denoting the inorder traversal of the tree.


Output Format
Return the root node of the binary tree.


Example Input
Input 1:
 A = [1, 2, 3]
 B = [2, 1, 3]
Input 2:
 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]


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


===========================
   CODE:
===========================

class TreeNode:
  def __init__(self, x)
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def buildTree(self, inorder, preorder):
    """
    inorder: array in form of inorder
    preorder: array in the form of preorder

    return:
    Tree constructed from inorder and preorder
    """

    return self.buildtree_from_inorder_preorder(inorder, preorder, 0, len(inorder) - 1, 0, len(preorder) - 1 )

  def buildtree_from_inorder_preorder(self, A, B, i1, j1, i2, j2):
    if i1 > j1:
      return None

    root = TreeNode(A[i1])

    idx = -1

    for i in range(i2, j2+1):
      if B[i] == A[i1]:
        idx = i 
        break

    count = idx - i2

    root.left = self.buildtree_from_inorder_preorder(A, B , i1+1, i1+count, i2, idx-1)
    root.right = self.buildtree_from_inorder_preorder(A, B, i1+count+1, j1, idx+1, j2 )

    return root


