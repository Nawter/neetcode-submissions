# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # create an empty stack and set curr = root
        stack = []
        curr = root

        # While stack is not empty or curr is not None
        # Push all the elements from the left side of the tree
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
        
        # Pop first element from the stack and this is the next smallest node
            curr = stack.pop()
        # Decrement k. If k ==0 return the node's value
            k -=1
            if k==0:
                return curr.val
        # move all the elements from the right
            curr = curr.right
        # Pop and Return the k-th smallest integer 
        