from sortedcontainers import SortedList
from bisect import bisect_right
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        l = SortedList()
        n, m = len(potions), len(spells)
        ans = [0] * m
        for potion in potions:
            l.add(success / potion)
        for i in range(m):
            index = bisect_right(l, spells[i])
            ans[i] = index
        return ans