class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        Max = 2 ** maximumBit - 1
        Ans = [0] * len(nums)
        temp = nums[0]
        Ans[0] = temp
        for i in range(1, len(nums)):
            temp = temp ^ nums[i]
            Ans[i] = temp

        for i in range(len(nums)):
            Ans[i] = Max ^ Ans[i]
        
        return Ans[::-1]
