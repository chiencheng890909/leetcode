class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        temp = [0] * (n - 1)
        for i in range(n - 1, 1, -1):
            for j in range(i, 0, -1):
                temp[j - 1] = str((int(s[j]) + int(s[j - 1])) % 10)
            s = temp[:]

        if s[0] == s[1]:
            return True
        return False
