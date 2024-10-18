class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = 0
        candidate = []
        for i in nums:
            Max = Max | i 
        
        for i in nums:
            Len = len(candidate)
            for j in range(Len):
                candidate.append(candidate[j])
                candidate[j] = candidate[j] | i
            candidate.append(i)

        Ans = sum([1 for can in candidate  if can == Max])
        
        return Ans
        
