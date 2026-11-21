# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, diameter):
            if not node:
                return diameter - 1
            res = 0
            res = max(res, dfs(node.left, 1) + dfs(node.right, 1))
            res = max(res, dfs(node.left, diameter + 1))
            res = max(res, dfs(node.right, diameter + 1))
            
            return res

        return dfs(root, 0) 