class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        temp = [0, 0, 0]
        for c in s:
            temp[ord(c) - ord('a')] += 1

        if min(temp) < k:
            return -1

        size = 0

        for c in range(len(s)):
            temp[ord(s[c]) - ord('a')] -= 1
            if min(temp) < k:
                temp[ord(s[size]) - ord('a')] += 1
                size += 1
        return size

