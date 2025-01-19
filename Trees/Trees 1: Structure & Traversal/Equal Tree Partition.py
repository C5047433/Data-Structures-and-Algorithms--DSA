Problem Description
Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.


Problem Constraints
1 <= size of tree <= 100000
0 <= value of node <= 109


Input Format
First and only argument is head of tree A.


Output Format
Return 1 if the tree can be partitioned into two trees of equal sum else return 0.


Example Input
Input 1:
 
                5
               /  \
              3    7
             / \  / \
            4  6  5  6
Input 2:
 
                1
               / \
              2   10
                  / \
                 20  2


Example Output
Output 1:
 1
Output 2:
 0


Example Explanation
Explanation 1:
 Remove edge between 5(root node) and 7: 
        Tree 1 =                                               Tree 2 =
                        5                                                     7
                       /                                                     / \
                      3                                                     5   6    
                     / \
                    4   6
        Sum of Tree 1 = Sum of Tree 2 = 18
Explanation 2:
 The given Tree cannot be partitioned.


===========================
CODE:
===========================

class TreeNode:
  def __init__(self, X):
    self.val = X
    self.left = None
    self.right = None


class Solution:
  def equal_partition(self, A):
    """
    Traverse through Tree to find if equal partition tree sum exists or not

    :param A: root of the give array
    :return True if equal sum parition tree exists otherwise False
    """

    #intialize to store all subtree sum in array
    subtree_sum = []

    #compute the totalsum of subtree
    total_sum = self.subtree_sum(A, subtree_sum)
    #print(total_sum, cumulative_sum)

    #if totalsum is odd, partitioning equally is not possible, return False.
    if  total_sum % 2 != 0:
      return False
    else:
      subtree_sum.pop()
      #if half sum is present in subtrr result array, return True
      half_sum = total_sum // 2
      return True if half_sum in subtree_sum else False


  def subtree_sum(self, node, subtree_sum):
    """
    Helper function to get the subtree sum at each root

    :node: param node represents root
    :cumulative_sum: store all subtree sums at every root
    :return sum of subtree
    """
    
    #Base Case: For node is None, return sum as zero
    if node is None:
      return 0

    leftsum = self.subtree_sum(node.left, subtree_sum)
    rightsum = self.subtree_sum(node.right, subtree_sum)

    #current subtree sum is sum of (left tree, right tree, root value)
    current_sum = leftsum + rightsum + node.val

    #append subtree sum to array
    subtree_sum.append(current_sum)

    return current_sum

#Input Tree 
a = TreeNode(5)
b = a.left = TreeNode(3)
c = b.left = TreeNode(4)
d = b.right = TreeNode(6)
e = a.right = TreeNode(7)
f = e.left = TreeNode(5)
g = e.right = TreeNode(6)


#create solution
solution = Solution()

#print the output
print(solution.equal_partition(a))
  
