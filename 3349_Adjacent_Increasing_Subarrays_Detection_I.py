class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l = set()
        if k == 1:
            return True
        for i in range(n - k + 1):
            temp = nums[i:i+k]
            if temp == sorted(temp) and len(set(temp)) == k:
                l.update(set([j for j in range(i, i + k)]))
                if set([j for j in range(i - k, i)]) <= l:
                    return True
        return False
