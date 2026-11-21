# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def levelOrder(node, level):
            if not node:
                return
            
            if len(levels) < level:
                levels.append([node.val])
            else:
                levels[level - 1].append(node.val)
            levelOrder(node.left, level + 1)
            levelOrder(node.right, level + 1)

        levelOrder(root, 1)

        return [level[-1] for level in levels]