# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        ans_1 = 0
        now_node = ans
        while l1 is not None or l2 is not None or ans_1 != 0:
            x_1 = l1.val if l1 is not None else 0
            x_2 = l2.val if l2 is not None else 0

            ans_0 = x_1 + x_2 + ans_1
            ans_1 = ans_0 // 10
            ans_0 = ans_0 % 10

            new_node = ListNode(ans_0)
            now_node.next = new_node
            now_node = now_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return ans.next
        
