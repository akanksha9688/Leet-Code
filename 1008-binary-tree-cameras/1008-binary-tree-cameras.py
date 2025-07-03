# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cnt=0
        if self.dfs(root)==0:
            self.cnt+=1
        return self.cnt
    def dfs(self,node):
        if node is None:
            return 1
        left=self.dfs(node.left)
        right=self.dfs(node.right)

        if left==0 or right ==0:
            self.cnt+=1
            return 2
        
        if left ==2 or right ==2:
            return 1
        else:
            return 0
        return -1
        