# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            nonlocal res
            
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        res = 0
        dfs(root)
        return res
