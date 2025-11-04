from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            temp = sorted(nums[i:i + k], reverse=True)
            count = Counter(temp)
            count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
            keys = list(count.keys())
            if len(keys) < x:
                ans[i] = sum(temp)
            else:
                ans[i] = sum([count[key] * key for key in keys[:x]])
        return ans