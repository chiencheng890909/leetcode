class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = len(energy)
        ans = [0] * (m + k)
        for i in range(m - 1, -1, -1):
            ans[i] = ans[i + k] + energy[i]
        return max(ans[:m]) 