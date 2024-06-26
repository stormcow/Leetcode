# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        return max(left_depth, right_depth)
