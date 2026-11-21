# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {}
        for i, node in enumerate(inorder):
            positions[node] = i
        
        preorder_index = 0
        def search(l, r):
            nonlocal preorder_index
            if preorder_index > len(preorder) - 1:
                return
            if l >= r:
                return

            node_to_add = preorder[preorder_index]
            mid = positions[node_to_add]
            if l > mid or r < mid:
                return
            node_to_add_node = TreeNode(node_to_add)
            preorder_index += 1
            node_to_add_node.left = search(l, mid)
            node_to_add_node.right = search(mid + 1, r)
            return node_to_add_node

        return search(0, len(inorder))