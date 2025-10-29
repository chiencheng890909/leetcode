class Solution:
    def smallestNumber(self, n: int) -> int:
        n = bin(n)[2:]
        n = ''.join(['1' for c in list(n)])
        return int(n, 2)
