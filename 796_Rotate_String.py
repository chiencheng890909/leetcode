class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = list(s)
        b = list(goal)
        if len(a) is not len(b):
            return False

        Size = len(a)
        for i in range(Size):
            if a == b:
                return True
            a.append(a.pop(0))
        return False

        
