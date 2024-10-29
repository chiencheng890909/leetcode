class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        temp = [[0] * len(grid[i]) for i in range(len(grid))]
        row = 0
        col = 1
        Ans = 0
        while col < len(grid[0]):
            row = 0
            while row < len(grid):
                if row + 1 < len(grid) and grid[row + 1][col - 1] < grid[row][col] and temp[row + 1][col - 1] >= temp[row][col]:
                    if col - 1 == 0 or temp[row + 1][col - 1] > 0:
                        temp[row][col] = temp[row + 1][col - 1] + 1
                        Ans = max(Ans, temp[row][col])
                if grid[row][col - 1] < grid[row][col] and temp[row][col - 1] >= temp[row][col]:
                    if col - 1 == 0 or temp[row][col - 1] > 0:
                        temp[row][col] = temp[row][col - 1] + 1
                        Ans = max(Ans, temp[row][col])
                if row > 0 and grid[row - 1][col - 1] < grid[row][col] and temp[row - 1][col - 1] >= temp[row][col]:
                    if col - 1 == 0 or temp[row - 1][col - 1] > 0:
                        temp[row][col] = temp[row - 1][col - 1] + 1
                        Ans = max(Ans, temp[row][col])
                row += 1
            col += 1
        # for Arr in grid:
        #     print(Arr)
        # print("--------------------------")
        # for Arr in temp:
        #     print(Arr)
        return Ans

