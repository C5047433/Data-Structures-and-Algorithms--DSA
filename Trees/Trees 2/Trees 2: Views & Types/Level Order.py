Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Problem Constraints
1 <= number of nodes <= 105


Input Format
First and only argument is root node of the binary tree, A.


Output Format
Return a 2D integer array denoting the level order traversal of the given binary tree.


Example Input
Input 1:
    3
   / \
  9  20
    /  \
   15   7
Input 2:
   1
  / \
 6   2
    /
   3


Example Output
Output 1:
 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:
 [ 
   [1]
   [6, 2]
   [3]
 ]


Example Explanation
Explanation 1:
 Return the 2D array. Each row denotes the traversal of each level.


================================
CODE:
================================

# Definition for a  binary tree node
class Treenode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

from collections import deque

class Solution:
      def level_order_traversal(self, A):
        """
        Travel and print all the element at each level till the leaf node

        :param A: TreeNode, the root of the tree
        :return: array of all intergers at each level
        """

        #intialize a array to append array of nodes at each level
        final = []
        #initalize a queue to add elements at at each level and use necessary deque functions 
        queue = deque()
        #if A is not empty then add element to q else return as empty
        if A is not None:
            queue.append(A)
            #intialize last to current node i.e root at the level
            #last  = A.val
        else:
            return []

        while len(queue) > 0:
            #at each level intialize a array to capture all the elements at the arrow
            ans = []
            #till the lenght of Q, remove first elemtn from the Q, add left child and right child if they exists 
            for i in range(len(queue)):
                x = queue.popleft()
                ans.append(x.val)

                if x.left is not None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
                    
            #Keep appending each level node elements and return the output   
            final.append(ans)
            
        return final
        
# Example usage
if __name__ == "__main__":
    a = Treenode(1)
    b = a.left = Treenode(2)
    c = a.right = Treenode(3)
    d = b.left = Treenode(4)
    e = b.right = Treenode(5)
    f = e.left = Treenode(7)
    g = f.right = Treenode(11)
    h = c.right = Treenode(6)
    i = h.left = Treenode(8)
    j = i.left = Treenode(10)
    k = h.right = Treenode(9)

    solution = Solution()
    print(solution.level_order_traversal(a))
