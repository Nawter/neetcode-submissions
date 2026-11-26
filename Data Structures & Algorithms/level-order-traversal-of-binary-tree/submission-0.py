# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS:maintain an empty list res where res[d] stores all
        # nodes at depth d
        res = []
        # create function dfs(node, depth)
        def dfs(node,depth):
        # if node is null return
            if not node:
                return None
        # if res has no list for this depth, create new list and
        # append new empty list
            if len(res) == depth:
                res.append([])
        # append the node's value to res[depth]
            res[depth].append(node.val)
        # recurse on node.left with depth+1
            dfs(node.left, depth+1)
        # recurse on node.right with depth+1
            dfs(node.right, depth+1)


        dfs(root,0)
        return res





