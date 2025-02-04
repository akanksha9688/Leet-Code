class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        j = 1
        sum_c = nums[i]
        max_sum = 0
        max_sum = max(max_sum, nums[i])
        while i < j and j < len(nums):
            if nums[j] > nums[j-1]:
                sum_c += nums[j]
                max_sum = max(max_sum, sum_c)
                j += 1

            else:
                sum_c = nums[j]
                i = j
                j += 1

        return max(max_sum, sum_c)
        