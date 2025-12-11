from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(lambda: [10**5,0])
        cols = defaultdict(lambda: [10**5,0])
        ans, m = 0, len(buildings)
        for i in range(m):
            rows[buildings[i][0]][0] = min(rows[buildings[i][0]][0], buildings[i][1])
            rows[buildings[i][0]][1] = max(rows[buildings[i][0]][1], buildings[i][1])

            cols[buildings[i][1]][0] = min(cols[buildings[i][1]][0], buildings[i][0])
            cols[buildings[i][1]][1] = max(cols[buildings[i][1]][1], buildings[i][0])

        for i in range(m):
            Min, Max = rows[buildings[i][0]]
            if Min < buildings[i][1] < Max:
                Min, Max = cols[buildings[i][1]]
                if Min < buildings[i][0] < Max:
                    ans += 1
        return ans