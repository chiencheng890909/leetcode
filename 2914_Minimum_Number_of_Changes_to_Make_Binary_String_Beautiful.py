class Solution:
    def minChanges(self, s: str) -> int:
        Ans = 0
        for i in range(0, len(s) - 1, 2):
            if s[i] != s[i + 1]:
                Ans += 1
        return Ans
