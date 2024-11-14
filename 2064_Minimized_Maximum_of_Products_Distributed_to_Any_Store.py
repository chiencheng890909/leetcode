class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if n == len(quantities):
            return max(quantities)

        left, right = 1, max(quantities)
        while left <= right:
            mid = (left + right) // 2
            temp = sum([ceil(quantity / mid) for quantity in quantities])
            if temp > n:
                left = mid + 1
            else:
                right = mid - 1

        return max(left, right)
