class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        return sum([1 if not any(word in brokenLetters for word in words[i]) else 0 for i in range(len(words))])
