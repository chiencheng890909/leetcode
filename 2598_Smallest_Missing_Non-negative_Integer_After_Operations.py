from collections import defaultdict
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        values = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] < 0:
                temp = value * (abs(nums[i] + 1) // value + 1) + nums[i]
            else:
                temp = nums[i] - value * (nums[i] // value)
            values[temp] += 1
        times = 0
        while True:
            for i in range(value):
                if values[i] == 0:
                    return value * times + i
                values[i] -= 1
            times += 1