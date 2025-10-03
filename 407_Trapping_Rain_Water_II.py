import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        heap = []
        for i in [0, m - 1]:
            for j in range(n):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1

        for j in [0, n - 1]:
            for i in range(m):
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1

        level, water = 0, 0
        while heap:
            z, x, y = heapq.heappop(heap)
            level = max(level, z)
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    if heightMap[i][j] < level:
                        water += level - heightMap[i][j]
                    heightMap[i][j] = -1
        return water

