import queue

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        Len = len(nums)
        Ans, temp = 0, 0
        Dict = defaultdict(int)

        for i in range(k):
            temp += nums[i]
            Dict[nums[i]] += 1
        if len(Dict) == k:
            Ans = temp

        for i in range(k, Len):
            temp -= nums[i - k]
            Dict[nums[i - k]] -= 1

            temp += nums[i]
            Dict[nums[i]] += 1

            if Dict[nums[i - k]] == 0:
                Dict.pop(nums[i - k])
            
            if len(Dict) == k:
                Ans = max(Ans, temp)
        return Ans
