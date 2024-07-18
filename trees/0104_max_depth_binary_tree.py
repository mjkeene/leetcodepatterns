# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS, use queue
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return level

        # Recursive DFS
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Iterative DFS (preorder)
        # if not root:
        #     return 0

        # stack = [(root, 1)]
        # res = 1

        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         res = max(res, depth)
        #         stack.append((node.left, depth + 1))
        #         stack.append((node.right, depth + 1))
        # return res
