# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subtree: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same_tree(root,subtree):
            return True
        return self.isSubtree(root.left,subtree) or self.isSubtree(root.right,subtree)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val != q.val:
                return False

        return self.is_same_tree(p.left,q.left) and self.is_same_tree(p.right,q.right)