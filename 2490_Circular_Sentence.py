class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        if len(words) == 1:
            temp = list(words[0])
            if temp[0] == temp[-1]:
                return True
            return False
        else:
            temp = list(words[-1])[-1]
            for word in words:
                if temp != list(word)[0]:
                    return False
                temp = list(word)[-1]
            return True
