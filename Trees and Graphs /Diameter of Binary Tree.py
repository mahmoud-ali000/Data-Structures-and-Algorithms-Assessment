# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], _min=0, _max=0) -> int:
        _min
        
        return _min + _max
    
    def find_min(self, root, height=0):
        if not root:
            return height-1
        return min(
            self.find_min(root.left, height+1),
            self.find_min(root.right, height+1)
        )
    
    def find_max(self, root, height=0):
        if not root:
            return height-1
        return max(
            self.find_max(root.left, height+1),
            self.find_max(root.right, height+1)
        )


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], _min=0, _max=0) -> int:
        
        self.max = 0

        def height(root):
            if not root:
                return 0
            
            left_h = height(root.left)
            right_h = height(root.right)
            self.max = max(self.max, left_h+right_h)
            return max(left_h, right_h)+1
        
        height(root)
        return self.max
