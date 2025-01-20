Problem Description
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.


Problem Constraints
1 <= number of nodes <= 10^5
-100000 <= B, value of nodes <= 100000


Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B denoting the sum.


Output Format
Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum. Else, return 0.


Example Input
Input 1:
 Tree:    5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

 B = 22
Input 2:
 Tree:    5
         / \
        4   8
       /   / \
     -11 -13  4

 B = -1


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:
 There exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which has sum 22. So, return 1.
Explanation 2:
 There is no path which has sum -1.


  =======================
  CODE:
  =======================

#Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
  """
  Travese throuigh Tree from root to leaf
  check if we can find sum of travel equals to B
  
	# @param A : root node of tree
	# @param B : integer: to find the path where we can see if value B can be found 
	# @return 1 if path exists else 0
  """
	def hasPathSum(self, A, B):

    node = A
    #Base case: if node is None, return 0
    if node is None:
      return 0

    #travel through the Tree in postorder, keep subtracting the node
    B -= node.val

    #At leaf Node, if B == 0, then path found, return 1
    if A.left is None and A.right is None and B == 0:
      return 1
    
    #if left node is present or right node is present, traverse recursively
    return self.hasPathSum(node.left, B) or self.hasPathSum(node.right, B)


# Example Usage:
a = TreeNode(5)
b = a.left = TreeNode(4)
c = b.left = TreeNode(11)
d = c.left = TreeNode(7)
e = c.right = TreeNode(2)
f = a.right = TreeNode(8)
g = f.left = TreeNode(13)
h = f.right = TreeNode(4)
i = h.right = TreeNode(1)

solution = Solution()
print(solution.hasPathSum(a, 22))  # Output: 1 (True)
print(solution.hasPathSum(a, 26))  # Output: 1 (True)
print(solution.hasPathSum(a, 10))  # Output: 0 (False)
    
