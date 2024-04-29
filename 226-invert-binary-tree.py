class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        tmp_node = root.right
        root.right = root.left
        root.left = tmp_node
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        return root
