class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = min(dp[i], dp[i + 1]) + n
        return dp[0]
        