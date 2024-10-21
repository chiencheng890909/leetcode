class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def backtrack(start, dic):
            if start == len(s):
                return 0
            Ans = 0
            for end in range(start + 1, len(s) + 1):
                temp = s[start:end]
                if temp not in dic:
                    dic.add(temp)
                    Ans = max(Ans, 1 + backtrack(end, dic))
                    dic.remove(temp)
            return Ans
        return backtrack(0, set())
        
