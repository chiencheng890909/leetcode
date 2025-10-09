class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        time = [0] * (n + 1)
        for i in range(m):
            for j in range(n):                        
                time[j + 1] = max(time[j + 1], time[j]) + skill[j] * mana[i]
            for j in range(n - 1, 0, -1):
                time[j] = time[j + 1] - skill[j] * mana[i]
        
        return time[n]