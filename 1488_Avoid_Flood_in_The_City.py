from sortedcontainers import SortedList
from bisect import bisect_right
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        cities = dict()
        days = SortedList()
        for day, loc in enumerate(rains):
            if rains[day] != 0:
                if loc in cities:
                    pre = cities[loc]
                    dry_day = days.bisect_right(pre)
                    if dry_day == len(days):
                        return []
                    ans[days[dry_day]] = loc
                    days.pop(dry_day)
                    cities[loc] = day
                else:
                    cities[loc] = day
            else:
                days.add(day)
                ans[day] = 1
        return ans
