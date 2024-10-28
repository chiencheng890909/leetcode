class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums = list(nums_set)
        index = 0
        Len = len(nums)
        Ans = 0
        while index < Len:
            temp = [nums[index]]
            tar = temp[-1] ** 2
            while tar in nums_set:
                temp.append(tar)
                tar = tar ** 2
            Ans = max(Ans, len(temp))
            index += 1

        if Ans < 2:
            return -1
        return Ans
