from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        inorder_map = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        inorder_visited = [False] * len(inorder)

        def build():
            root = TreeNode(preorder.popleft())
            inorder_visited[ inorder_map[root.val] ] = True
            
            if (
                inorder_map[root.val] -1 >= 0 and 
                not inorder_visited[
                    inorder_map[root.val] -1
                ]
            ):
                root.left = build()
            else:
                root.left = None
            
            if (
                inorder_map[root.val] +1 < len(inorder) and 
                not inorder_visited[
                    inorder_map[root.val] +1
                ]
            ):
                root.right = build()
            else:
                root.right = None

            return root

        return build()



        inorder_map = dict()
        inorder_visited = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
            inorder_visited[inorder[i]] = False

        def build():
            root = TreeNode(preorder[0])
            root.left = build

            root.left = TreeNode(left[-1]) if (left:=inorder[
                :inorder_map[preorder[0]]+1
            ]) else None
            root.right = TreeNode(right[0]) if (right:=inorder[
                inorder_map[preorder[0]]+1:
            ]) else None
            
            return root
        
        def build(pointer=0):
            print(pointer, preorder[pointer])
            if inorder_visited[preorder[pointer]]:
                return None
            root = TreeNode(preorder[pointer])
            inorder_visited[preorder[pointer]] = True
            # has left
            if inorder_map[preorder[pointer]] -1 >= 0:
                root.left = build(pointer+1)
            else:
                root.left = None

            # has right
            if 1 + inorder_map[preorder[pointer]] < len(preorder):
                root.right = build(
                    1 + inorder_map[preorder[pointer]]
                )
            else:
                root.right = None

            return root

        return build()
print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))
