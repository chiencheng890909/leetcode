class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        temp =[[0] * (n + 1) for i in range(n + 1)] 
        ans = [[0] * n for i in range(n)]
        for r1, c1, r2, c2 in queries:
            temp[r1][c1] += 1
            temp[r1][c2 + 1] -= 1
            temp[r2 + 1][c1] -= 1
            temp[r2 + 1][c2 + 1] += 1

        for i in range(n):
            for j in range(n):
                top = ans[i - 1][j] if i > 0 else 0
                left = ans[i][j - 1] if j > 0 else 0
                top_left = ans[i - 1][j - 1] if i > 0 and j > 0 else 0
                ans[i][j] = temp[i][j] + top + left - top_left
        return ans