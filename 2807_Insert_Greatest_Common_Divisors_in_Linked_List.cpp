/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int GCD(int A, int B) {
        int C;
        if (A < B) {
            C = B;
            B = A;
            A = C;
        }

        while (B > 0) {
            C = A % B;
            A = B;
            B = C;
        }
        return A;
    }

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* pre = head;
        ListNode* cur = head->next;
        int num;
        if (cur == nullptr)
            return head;

        while(cur != nullptr) {
            num = gcd(pre->val, cur->val);
            pre->next = new ListNode(num, cur);
            pre = cur;
            cur = cur->next;
        }
        return head;
    }
};
