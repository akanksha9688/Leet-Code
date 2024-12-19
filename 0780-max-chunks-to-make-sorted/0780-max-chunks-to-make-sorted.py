class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk_max = deque()
        for i in arr:
            temp = i
            if (len(chunk_max) > 0) and (i < chunk_max[-1]):
                temp = chunk_max.pop()
                while (len(chunk_max) > 0) and (i < chunk_max[-1]):
                    chunk_max.pop()
            chunk_max.append(temp)
        return len(chunk_max)
