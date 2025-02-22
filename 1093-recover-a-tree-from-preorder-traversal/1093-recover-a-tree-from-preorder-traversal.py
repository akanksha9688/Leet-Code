# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()
        def helper(d, string, node):
            v = '-'*d
            lst = re.split(rf'(?<!-){v}(?!-)', string)
            node.val = int(lst[0])
            if len(lst)>1:
                node.left = TreeNode()
                helper(d+1, lst[1], node.left)
            if len(lst)>2:
                node.right = TreeNode()
                helper(d+1, lst[2], node.right)
        helper(1, traversal, root)
        return root