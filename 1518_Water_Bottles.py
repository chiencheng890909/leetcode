class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        Ans = 0 
        emptyBottles = 0
        while numBottles > 0:
            Ans += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
        return Ans