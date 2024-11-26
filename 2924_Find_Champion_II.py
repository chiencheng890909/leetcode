class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        Ans = set([i for i in range(n)])
        for edge in edges:
            Ans.discard(edge[1])
        if len(Ans) == 1:
            return next(iter(Ans))
        return -1
