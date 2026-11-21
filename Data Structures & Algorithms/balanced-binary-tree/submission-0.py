# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        
        def dfs(node, depth):
            nonlocal is_balanced
            if not node:
                return depth

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if not abs(left - right) <= 1:
                is_balanced = False

            return max(left, right)

        dfs(root, 1)
        return is_balanced