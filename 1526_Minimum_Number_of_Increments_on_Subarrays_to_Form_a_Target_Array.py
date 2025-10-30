class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev, ans = 0, 0
        for tar in target:
            if tar > prev:
                ans += (tar - prev)
            prev = tar
        return ans
