class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        freq = {}
        res = -1

        for num in nums:
            key = self.digitSum(num)
            if key in freq:
                res = max(res, freq[key] + num)
                freq[key] = max(freq[key], num)
            else:
                freq[key] = num

        return res

    def digitSum(self, n):
        return sum(int(digit) for digit in str(n))