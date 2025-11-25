class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem, ans = 1 % k, 1
        if k % 2 == 0 or k % 5 == 0:
            return -1

        while rem != 0:
            rem = (rem * 10 + 1) % k
            ans += 1
        return ans
