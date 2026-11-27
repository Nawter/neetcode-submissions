# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # If tree is empty return True
        if not root:
            return True
        # Push (root, leftBound, rightBound) into a queue
        q = deque([(root, float("-inf"), float("inf"))])
        # while the queue is not empty
        while q:
        # Pop element (node, leftBound, rightBound)
            node, left, right = q.popleft()
        # If node.val not between leftBound and rightBound 
            if not (left < node.val < right):
                return False
        # return False
        # Push left child with range (node.left, leftBound, value)
            if node.left:
                q.append((node.left, left, node.val))
        # Push right child with range(node.right, value, rightBound)
            if node.right:
                q.append((node.right, node.val, right))

        return True
        