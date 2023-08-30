# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# take advantage of the contraint - All Node.val are unique.

#   (approach 1) top-down
#   1. they can be at the same side (you will meet one first then the second on the same route)
#       the LCA would be the higher(p, q)
#   2. different side
#       record the parent before you meet any of them...(?) not gonna work
#   (approach 2) bottom-up
#   recursive return parent once we hit the p or q
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # find p,q first

        # find the LCA
        pass
