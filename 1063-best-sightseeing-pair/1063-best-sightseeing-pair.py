class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        max_prev_value = values[0]  # Keeps track of the max values[i] + i seen so far

        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j)
            max_score = max(max_score, max_prev_value + values[j] - j)

            # Update max_prev_value for the next iteration
            max_prev_value = max(max_prev_value, values[j] + j)

        return max_score
        