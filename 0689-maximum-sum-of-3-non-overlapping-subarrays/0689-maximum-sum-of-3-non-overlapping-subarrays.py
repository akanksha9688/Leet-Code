class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[-1 for _ in range(4)] for _ in range(n + 1)]
        def F(idx: int, K_Size_windowSum: List[int], k: int, left: int) -> int:
            if idx >= len(K_Size_windowSum):
                return 0 if left == 0 else float('-inf')
            if left < 0:
                return float('-inf')
            if dp[idx][left] != -1:
                return dp[idx][left]
            take_ith_index = K_Size_windowSum[idx] + F(idx + k, K_Size_windowSum, k, left - 1)
            not_take_ith_index = F(idx + 1, K_Size_windowSum, k, left)
            dp[idx][left] = max(take_ith_index, not_take_ith_index)
            return dp[idx][left]
        def recover(K_Size_windowSum: List[int], k: int, idx: int, t: int, res: List[int]):
            if idx >= len(K_Size_windowSum) or t == 0:
                return
            take_ith_index = K_Size_windowSum[idx] + F(idx + k, K_Size_windowSum, k, t - 1)
            not_take_ith_index = F(idx + 1, K_Size_windowSum, k, t)
            if take_ith_index >= not_take_ith_index:
                res.append(idx)
                recover(K_Size_windowSum, k, idx + k, t - 1, res)
            else:
                recover(K_Size_windowSum, k, idx + 1, t, res)
        P = [0] * n
        P[0] = nums[0]
        for i in range(1, n):
            P[i] = P[i - 1] + nums[i]
        K_Size_windowSum = [0] * (n - k + 1)
        for i in range(n - k + 1):
            if i == 0:
                K_Size_windowSum[0] = P[k - 1]
            else:
                K_Size_windowSum[i] = P[i + k - 1] - P[i - 1]
        res = []
        F(0, K_Size_windowSum, k, 3)
        recover(K_Size_windowSum, k, 0, 3, res)
        return res