class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []
        pre = ""
        for word in words:
            temp = ''.join(sorted(word))
            if temp != pre:
                ans.append(word)
                pre = temp
        return ans
