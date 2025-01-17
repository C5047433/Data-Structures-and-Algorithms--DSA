Problem Description
Given a binary tree, return the preorder traversal of its nodes values.


Problem Constraints
1 <= number of nodes <= 10^5


Input Format
First and only argument is root node of the binary tree, A.


Output Format
Return an integer array denoting the preorder traversal of the given binary tree.


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
 [1, 2, 3]
Output 2:
 [1, 6, 2, 3]


Example Explanation
Explanation 1:
 The Preoder Traversal of the given tree is [1, 2, 3].
Explanation 2:
 The Preoder Traversal of the given tree is [1, 6, 2, 3].


=======================================
CODE Using Recursion:
=======================================

class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None

class Solution:

  def preorder(self, A):
     """
     Travel through tree in preorder format using recursion.
     
     :A: root of the Tree
     :return thh prorder as an array 
     """
    result = []
    self.preorder_traversal(A, result)
    return result

  def preorder_traversal(self, root, result):

      #Base case:
      if root is None:
        return

      #preorder, append root, go left, then right
      result.append(root.val)
      self.preorder_traversal(root.left, result)
      self.preorder_traversal(root.right, result)


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
print(solution.preorder(a))


===========================================
CODE using Iterative method:
===========================================

class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None

from collections import deque

class Solution:

  def preorder_iterative(self, A):
    """
    Travel through tree in preorder format using iteration.
     
    :A: root of the Tree
    :return thh prorder as an array 
    """
    stack = deque()
    result = []

    current = A

    # iterate till current is empty or stack is empty
    while current is not None or len(stack) > 0:
        if current is None:
           #if current is none, move to right
            x = stack.pop()
            current = x.right
        else:
           #if current is not none, append to stack and array then move left of tree
            stack.append(current)
            result.append(current.val)
            current = current.left

    return result


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



solution = Solution()

print(solution.preorder_iterative(a))
