class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        node, color = {}, {}
        ans = []

        for x, y in queries:
            if x in node:
                prev_color = node[x]
                if prev_color == y:
                    ans.append(len(color))
                    continue
                if color[prev_color] == 1:
                    del color[prev_color]
                else:
                    color[prev_color] -= 1

            node[x] = y
            color[y] = color.get(y, 0) + 1
            ans.append(len(color))

        return ans

        