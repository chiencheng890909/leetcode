class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        temp, n = set([s]), len(s)
        q, ans = [s], s
        while q:
            chars = q.pop(0)
            ans = min(ans, chars)
            chars = list(chars)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)
            if added not in temp:
                temp.add(added)
                q.append(added)
            rotated = ''.join(chars[-b:] + chars[:-b])
            if rotated not in temp:
                temp.add(rotated)
                q.append(rotated)
        return ans 