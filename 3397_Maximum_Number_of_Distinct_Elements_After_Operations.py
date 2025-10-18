from collections import Counter
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        times = Counter(nums)
        rem, ans, keys = -k - 1, 0, sorted(times.keys())
        for key in keys:
            temp = max(rem, key - k - 1)
            if temp + times[key] > key + k:
                rem = key + k
            else:
                rem = temp + times[key]
            ans += (rem - temp)
        return ans