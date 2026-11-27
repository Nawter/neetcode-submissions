# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # create empty stack and set curr to root
        stack = []
        curr = root
        
        # while stack is not empty or curr is not None
        while stack or curr:
            # while curr is not empty transverse through the left side and append each node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # pop from the stack the next smallest element
            curr = stack.pop()
            #decrement k, if k is zero return the smallest element
            k -= 1
            if k == 0:
                return curr.val
            # move to the right side of the tree
            curr = curr.right