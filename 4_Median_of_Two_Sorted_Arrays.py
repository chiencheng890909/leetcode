class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ans_0 = 0
        ans_1 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        i = 0
        j = 0
        for _ in range((len_1 + len_2) // 2 + 1):
            ans_0 = ans_1
            if i < len_1 and j < len_2:
                if nums1[i] > nums2[j]:
                    ans_1 = nums2[j]
                    j+=1
                else:
                    ans_1 = nums1[i]
                    i+=1
            elif i < len_1:
                ans_1 = nums1[i]
                i+=1
            else:
                ans_1 = nums2[j]
                j+=1
        if (len_1 + len_2) % 2 == 1:
            return ans_1
        else:
            return((ans_1 + ans_0) / 2.0)
        
