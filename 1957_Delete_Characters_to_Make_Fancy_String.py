class Solution:
    def makeFancyString(self, s: str) -> str:
        pre = ""
        Ans = ""
        Del = False
        for c in s:
            if Del and c is pre:
                pre = c
            elif c is pre:
                Ans += c
                Del = True
                pre = c
            else:
                Ans += c
                Del = False
                pre = c

        return Ans
