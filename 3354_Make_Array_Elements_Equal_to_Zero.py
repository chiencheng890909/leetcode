class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        if n == 1:
            return 2
        left, right = 0, sum(nums[1:])
        for i in range(n):
            if nums[i] == 0:
                if left == right:
                    ans += 2
                elif left == right + 1 or right == left + 1:
                    ans += 1
            left += nums[i]
            if i + 1 < n:
                right -= nums[i + 1] 
        return ans