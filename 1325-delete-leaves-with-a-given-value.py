# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if (
            root.left
            and root.left.left is None
            and root.left.right is None
            and root.left.val == target
        ):
            root.left = None
        if (
            root.right
            and root.right.left is None
            and root.right.right is None
            and root.right.val == target
        ):
            root.right = None
        if not root.right and not root.left and root.val == target:
            return None
        return root
