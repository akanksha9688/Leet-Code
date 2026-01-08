class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)#row
        m=len(nums2)#col
        dp=[[float('-inf')]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][m]=float('-inf')
        for j in range(m+1):
            dp[n][j] =float('-inf')

        ans = self.solve(nums1, nums2, 0, 0, n, m, dp)
        return ans
    def solve(self,nums1,nums2,i,j,n,m,dp):
        if i==n or j==m:
            return float('-inf')

        if dp[i][j]!=float('-inf'):
            return dp[i][j]
        
        a=nums1[i]*nums2[j] + max(self.solve(nums1, nums2, i+1, j+1, n, m, dp),0)
        b=max(self.solve(nums1, nums2, i+1, j, n, m, dp),self.solve(nums1, nums2, i, j+1, n, m, dp))
        dp[i][j]=max(a,b)
        return dp[i][j]