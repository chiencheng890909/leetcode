class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = n - 1
        Ans = 0
        while i > 0:
            while j > 0:
                Ans += matrix[i][j]
                if matrix[i - 1][j - 1] > 0:
                    temp = min([matrix[i][j], matrix[i - 1][j], matrix[i][j - 1]])
                    if temp > 0:
                        matrix[i - 1][j - 1] = temp + 1
                j -= 1
            i -= 1
            j = n - 1
            
        return Ans + sum(matrix[0]) + sum(arr[0] for arr in matrix) - matrix[0][0]
