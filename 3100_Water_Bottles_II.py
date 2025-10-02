class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        Ans = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            Ans += 1
            emptyBottles -= (numExchange - 1)
            numExchange += 1
        return Ans