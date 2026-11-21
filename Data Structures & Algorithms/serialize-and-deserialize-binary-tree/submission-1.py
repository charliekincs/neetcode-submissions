# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder = ''

        def traverse(node):
            nonlocal preorder
            if not node:
                preorder = preorder[:] + '#,'
                return

            preorder = preorder[:] + str(node.val) + ','
            
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return preorder[:-1]


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')

        preorder_idx = 0
        def build():
            nonlocal preorder_idx
            val = preorder[preorder_idx]
            if val == '#':
                preorder_idx += 1
                return
            
            node = TreeNode(val)
            preorder_idx += 1
            node.left = build()
            node.right = build()
            return node
        
        return build()


