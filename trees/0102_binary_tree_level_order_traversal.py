# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Iterative BFS
        res = []
        if not root:
            return res

        q = collections.deque()
        q.append(root)
        res.append([root.val])
        while q:
            new_list = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    new_list.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    new_list.append(curr.right.val)
                    q.append(curr.right)
            if new_list:
                res.append(new_list)

        return res
