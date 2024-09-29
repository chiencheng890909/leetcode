class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        index = 0
        ans = s[0]
        last = 1
        while last < len(s):
            while s[last] in s[index:last]:
                index += 1
            if len(ans) < len(s[index:last + 1]):
                ans = s[index:last + 1]
            last += 1
        
        return(len(ans))

        
