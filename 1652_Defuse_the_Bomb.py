class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        Len = len(code)
        Ans = [0] * Len

        if k != 0:
            if k > 0:
                for i in range(Len):
                    Ans[i] = sum([code[(i + j + Len) % Len] for j in range(1, k + 1)])
            else:
                for i in range(Len):
                    Ans[i] = sum([code[(i + j + Len) % Len] for j in range(-1, k - 1, -1)])

        return Ans
