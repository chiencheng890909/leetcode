class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, pre = 0, 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] != colors[pre]:
                ans += sum(sorted(neededTime[pre: i])[:-1])
                pre = i
        ans += sum(sorted(neededTime[pre:])[:-1])
        return ans