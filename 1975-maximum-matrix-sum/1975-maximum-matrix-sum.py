class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_cnt = 0
        total_sum = 0
        mini = 10**32
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negative_cnt += 1
                    total_sum += -matrix[i][j]
                    mini = min(mini, -matrix[i][j])
                else:
                    total_sum += matrix[i][j]
                    mini = min(mini, matrix[i][j])
        if negative_cnt % 2 == 1:
            return total_sum - 2*mini
        else:
            return total_sum