# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
            
             
        max_depth_l = self.maxDepth(root.left) + 1
        max_depth_r = self.maxDepth(root.right) + 1


        return max(max_depth_l,max_depth_r)