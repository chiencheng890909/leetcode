class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n, ans = len(bank), 0
        pre = sum(1 if d == '1' else 0 for d in list(bank[0]))
        for i in range(1, n):
            take = sum(1 if d == '1' else 0 for d in list(bank[i]))
            if take:
                ans += pre * take
                pre = take
        return ans