# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node.left and not node.right and node.val == target:
                return True

            if node.left and dfs(node.left):
                node.left = None
            if node.right and dfs(node.right):
                node.right = None
            if not node.left and not node.right and node.val == target:
                return True

            return False
        
        dfs(root)
        if not root.left and not root.right and root.val == target:
            return None
        return root