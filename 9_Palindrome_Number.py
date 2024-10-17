class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        sen = list(str(x))
        i = 0
        j = len(sen) - 1
        while(i < j):
            if(sen[i] == sen[j]):
                i += 1
                j -= 1
            else:
                return False
        return True

        
