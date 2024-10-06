class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """        
        sen1 = sentence1.split()
        sen2 = sentence2.split()
            
        len1 = len(sen1)
        len2 = len(sen2)
        if len1 < len2:
            sen1, sen2 = sen2, sen1
            len1, len2 = len2, len1
        
        start = 0
        end = 0

        while start < len2 and sen1[start] == sen2[start]:
            start += 1
        while end < len2 and sen1[len1 - end - 1] == sen2[len2 - end - 1]:
            end += 1
        
        return start + end >= len2
        

