class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n, temp = len(nums), 0
        ans = [False] * n
        for i in range(n):
            temp = temp * 2 + nums[i]
            if not temp % 5:
                ans[i] = True
        return ans
