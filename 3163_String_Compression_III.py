class Solution:
    def compressedString(self, word: str) -> str:
        num = 1
        char = list(word)[0]
        Ans = ""
        for c in list(word)[1:]:
            if c == char and num < 9:
                num += 1
            else:
                Ans += (str(num) + char) 
                char = c
                num = 1
        
        Ans += (str(num) + char)
        return Ans
