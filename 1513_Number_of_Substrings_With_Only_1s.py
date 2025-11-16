class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        ans, pre = 0, 0
        for i in range(n):
            if s[i] == '0':
                ans += (i - pre + 1) * (i - pre) // 2
                pre = i + 1
        ans += (n - pre + 1) * (n - pre) // 2
        return ans % (10**9+7)
