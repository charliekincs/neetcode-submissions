# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def search(node):
            if (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
                return node
            if node.val == p.val or node.val == q.val:
                return node
            if p.val < node.val and q.val < node.val:
                return search(node.left)
            if p.val > node.val and q.val > node.val:
                return search(node.right)

        return search(root)