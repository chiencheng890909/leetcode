class Solution(object):
    def sim(self, n):
        s = [0]
        for x in range(n - 1):
            temp = s[::-1]
            s.append(1)
            for i in temp:
                s.append(1 - i)
        return ''.join(map(str,s))
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # S1 = "0"
        # Si = Si - 1 + "1" + reverse(invert(Si - 1))
        if n == 1:
            return str(0)

        ans = self.sim(n)
        return ans[k - 1]
