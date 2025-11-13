class Solution:
    def maxOperations(self, s: str) -> int:
        s, n = list(s), len(s)
        index = [i for i in range(n) if s[i] == '1']
        if len(index) == 0:
            return 0

        ans, pre = 0, -1
        temp = 0
        for i in index:
            if i != pre + 1:
                ans += temp
            temp += 1
            pre = i

        if index[-1] != n - 1:
            ans += temp
        return ans