class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, n = 0, len(prices)
        pre, times = 0, 0
        for i in range(n):
            if pre == prices[i] + 1:
                times += 1
                ans += times
            else:
                times = 1
                ans += times
            pre = prices[i]
        return ans