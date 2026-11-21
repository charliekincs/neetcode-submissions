# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def dfs(node, level):
            if not node:
                return
            
            dfs(node.left, level + 1)
            if len(levels) == level:
                levels.append(node.val)
            else:
                while len(levels) <= level:
                    levels.append(0)
                levels[level] = node.val
            dfs(node.right, level + 1)

        dfs(root, 0)
        return levels
