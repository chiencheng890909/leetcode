import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans, n = {"electronics":[], "grocery":[], "pharmacy":[], "restaurant":[]}, len(code)
        categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(n):
            if isActive[i]:
                if businessLine[i] in categories:
                    temp = re.findall(r'([\w_]*)', code[i])
                    if len(temp) == 2:
                        ans[businessLine[i]].append(code[i])
        results = []
        for key in categories:
            results.extend(sorted(ans[key]))
        return results