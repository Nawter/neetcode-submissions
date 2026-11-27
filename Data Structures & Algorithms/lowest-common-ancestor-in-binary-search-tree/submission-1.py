# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST is ordered this way
        # left subtree < node < right subtree
        # set cur = root        
        cur = root
        # while cur is not null        
        while cur:
            # if p.val and q.val are both greater than cur.val go right            
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # else if both smaller go left
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # otherwise you found first node return cur
            # return null if the tree is empty
            else:
                return cur



        