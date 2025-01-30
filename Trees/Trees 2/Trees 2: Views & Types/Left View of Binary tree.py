Problem Description
Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
NOTE: The value comes first in the array which have lower level.


Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9


Input Format
First and only argument is a root node of the binary tree, A.


Output Format
Return an integer array denoting the left view of the Binary tree.


Example Input
Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:
 [1, 2, 4, 8]
Output 2:
 [1, 2, 4, 5]


Example Explanation
Explanation 1:
 The Left view of the binary tree is returned.


======================
  CODE:
======================
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

from collections import deque
class Solution:
  def leftview(self, A):
    """
    A: root of the node

    return: list of elements in the tree from left view 
    """

    #intialize a Queue and result as list
    queue = deque()
    result = []

    #if A is not None, append to queue, result and update value to the last
    if A is not None:
      queue.append(A)
      last = A
      result.append(queue[0].val)
    else:
      #return empty list if A is empty
      return [] 

    #iteratea over the queue till empty
    while queue:
      #pop the leftmost element
      x = queue.popleft()

      #if x.left exists append to queue
      if x.left is not None:
        queue.append(x.left)
      
      #if x.right exists append to queue
      if x.right is not None:
        queue.append(x.right)

      #ig Queue is not empty and last matches to X, then append the first value in the queue which is ideally the left view element
      if last == x and queue:
        result.append(queue[0].val) #append the left view element value 
        last = queue[-1] #update the last with top elements from queue
    
    #return result
    return result


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

sol = Solution()
print(sol.left_view(root))  # Output: [1, 2, 4, 8]
