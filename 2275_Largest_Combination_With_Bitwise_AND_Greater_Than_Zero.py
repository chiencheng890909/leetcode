class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        Ans = 0
        for i in range(32):
            Ans = max(Ans, sum(1 for candidate in candidates if candidate & (1 << i)))
        return Ans
