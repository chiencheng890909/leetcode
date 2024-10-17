class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        Ans = num
        number = str(num)
        for i in range(9, 0, -1):
            index_2 = number.rfind(str(i))

            if(index_2 != -1):
                index_1 = -1
                for j in range(index_2):
                    if number[j] < number[index_2]:
                        index_1 = j  
                        break
                if(index_1 != -1):
                    temp = list(number)
                    temp[index_1], temp[index_2] = temp[index_2], temp[index_1]
                    Ans = max(Ans, int(''.join(temp)))
                    return Ans

        return Ans

        
