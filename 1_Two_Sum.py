class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        past = {}
        for index in range(len(nums)):
            if target - nums[index] in past:
                return [past[target - nums[index]], index]
            past[nums[index]] = index
        
