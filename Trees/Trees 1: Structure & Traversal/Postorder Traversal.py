Problem Description
Given a binary tree, return the Postorder traversal of its nodes values.


Problem Constraints
1 <= number of nodes <= 105


Input Format
First and only argument is root node of the binary tree, A.


Output Format
Return an integer array denoting the Postorder traversal of the given binary tree.


Example Input
Input 1:
   1
    \
     2
    /
   3
Input 2:
   1
  / \
 6   2
    /
   3


Example Output
Output 1:
 [3, 2, 1]
Output 2:
 [6, 3, 2, 1]


Example Explanation
Explanation 1:
 The Preoder Traversal of the given tree is [3, 2, 1].
Explanation 2:
 The Preoder Traversal of the given tree is [6, 3, 2, 1].

===========================
CODE
===========================


class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None

from collections import deque

class Solution:

  def postorder(self, A):
    """
    Travel through tree in postorder format using recursion.

    :A: root of the Tree
    :return thh postorder as an array
    """

    result = []
    self.postorder_recursion(A, result)
    return result

    node = A

  def postorder_recursion(self, node, result):
    """
    Helper function to recursively perform postorder traversal.

    :param node: TreeNode, the current node
    :param result: list, the traversal result being constructed
    """
    
    #Base case, if node is None return
    if node is None:
      return 
    
    #In postorder, add left, then right and finally root element to the result 
    self.postorder_recursion(node.left, result)
    self.postorder_recursion(node.right, result)
    result.append(node.val)

      


#create input
a = TreeNode(4)
b = a.left = TreeNode(0)
c = b.left = TreeNode(-1)
d = b.right = TreeNode(3)
e = a.right = TreeNode(10)
f = e.left = TreeNode(7)
g = e.right = TreeNode(15)
h = f.left = TreeNode(6)
i = f.right = TreeNode(9)
k = c.left = TreeNode(-4)
l = k.left = TreeNode(-7)


#create solution
solution = Solution()

#print solution
print(solution.postorder(a))
