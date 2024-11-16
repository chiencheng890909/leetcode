class Solution:
    def Is_increase(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                return False
        return True

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        Ans = [-1] * (n - k + 1)
        for i in range(n - k + 1):
            temp = nums[i:i + k]
            if self.Is_increase(temp):
                Ans[i] = temp[-1]
        return Ans
        
