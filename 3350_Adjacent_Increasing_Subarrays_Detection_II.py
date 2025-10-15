class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [False] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                temp[i - 1] = True
        ans, take = 1, [0]
        for i in temp:
            if i:
                take[-1] += 1
            else:
                take.append(0)
        if len(take) == 1:
            ans = (take[0] + 1) // 2
        else:
            for i in range(1, len(take)):
                ans = max((take[i - 1] + 1) // 2, ans)
                if take[i - 1] > 0 and take[i] > 0:
                    ans = max(min(take[i - 1], take[i]) + 1, ans)
            ans = max((take[-1] + 1) // 2, ans)
        return ans