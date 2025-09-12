class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v="aeiou"
        count=0
        for a in s:
            if a in v:
                count+=1
                break
        return bool(count)

        