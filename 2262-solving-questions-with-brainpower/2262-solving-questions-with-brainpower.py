class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n

        return self.helper(questions,0,dp,n)

    def helper(self,q : List[List[int]] ,idx :int ,dp: List[int],n :int):
        if idx >= n:
            return 0

        if dp[idx] != -1:
            return dp[idx]

        points = q[idx][0]
        skip = self.helper(q,idx + 1,dp,n)
        solve = self.helper(q,idx + q[idx][1] + 1,dp,n) + points

        dp[idx] = max(skip, solve)
        return dp[idx]
        