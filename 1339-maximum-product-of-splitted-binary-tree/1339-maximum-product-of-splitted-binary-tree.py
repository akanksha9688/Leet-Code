# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.total = 0

        def dfs(node):
            if not node:
                return 0

            curr = node.val + dfs(node.left) + dfs(node.right)
            self.ans = max(self.ans, (self.total - curr) * curr)
            return curr

        self.total = dfs(root)  # total tree sum
        dfs(root)               # compute max product
        return self.ans % (10**9 + 7)

        