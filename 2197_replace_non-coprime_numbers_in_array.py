class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def GCD(A: int, B: int):
            temp = A % B
            if temp == 0:
                return B
            else:
                return GCD(B, temp)
        
        def LCM(A: int, B: int, gcd: int):
            return A * B // gcd
        
        index = 1
        if len(nums) < 2:
            return nums
            
        Ans = [nums[0], nums[1]]
        gcd = 0
        while index + 1 < len(nums):
            if len(Ans) < 2 or gcd == 1:
                index += 1
                if index < len(nums):
                    Ans.append(nums[index])
                
            if Ans[-1] < Ans[-2]:
                gcd = GCD(Ans[-2], Ans[-1])
            else:
                gcd = GCD(Ans[-1], Ans[-2])

            if gcd > 1:
                temp = LCM(Ans[-1], Ans[-2], gcd)
                Ans.pop()
                Ans[-1] = temp
        return Ans


            
