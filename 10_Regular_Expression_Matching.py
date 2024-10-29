class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        temp = re.match(p, s)
        if temp is None:
            return False
        Len = list(temp.span())
        return Len[1] - Len[0] == len(s)
