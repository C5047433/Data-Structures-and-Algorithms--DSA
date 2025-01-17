Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.


Problem Constraints
1 <= number of nodes <= 105


Input Format
First and only argument is root node of the binary tree, A.


Output Format
Return an integer array denoting the inorder traversal of the given binary tree.


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
 [1, 3, 2]
Output 2:
 [6, 1, 3, 2]


Example Explanation
Explanation 1:
 The Inorder Traversal of the given tree is [1, 3, 2].
Explanation 2:
 The Inorder Traversal of the given tree is [6, 1, 3, 2].

==========================
CODE using recursion
==========================


class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None

class Solution:

  def inorder(self, A):
    """
    Travel through tree in preorder format using recursion.
    
    :A: root of the Tree
    :return thh prorder as an array 
    """

    result = []
    self.inorder_recursion(A, result)
    return result

  def inorder_recursion(self, node, result):

    #Base Case: if node is None, return
    if node is None:
      return

    #inorder travesal, append left, root node, then append right
    self.inorder_recursion(node.left, result)
    result.append(node.val)
    self.inorder_recursion(node.right, result)

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
print(solution.inorder(a))



==========================
CODE using iteration 
==========================

class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None

from collections import deque

class Solution:

  def inorder(self, A):
    """
    Travel through tree in preorder format using iteration.
    
    :A: root of the Tree
    :return thh prorder as an array 
    """
    stack = deque()
    result = []

    node = A

    while node is not None or len(stack) > 0:
      #if node is none, append root node to result and move right
      if node is None:
        x = stack.pop()
        result.append(x.val)
        node = x.right
      else:
      #if node is not none, append rto stack and move left
        stack.append(node)
        node = node.left


    return result


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
print(solution.inorder(a))

  
