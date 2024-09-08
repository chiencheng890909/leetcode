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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {

        if (head == nullptr) {
            vector<ListNode*> Ans(k);
            return Ans;
        }

        int size = 0;
        int q, r;
        int Length;
        ListNode* cur;
        vector<ListNode*> Ans;

        cur = head;
        while(cur != nullptr) {
            size ++;
            cur = cur->next;
        }
        
        q = size / k;
        r = size % k;

        for(int i = 0; i < k; i++) {
            if (i < r)
                Length = q + 1;
            else
                Length = q;

            if (Length == 0)
                Ans.push_back(nullptr);
            else {
                cur = new ListNode(); 
                Ans.push_back(cur);
                for(; Length > 0; Length--) {
                    cur->val = head->val;
                    if (Length == 1)
                        cur->next = nullptr;
                    else 
                        cur->next = new ListNode();
                    head = head->next;
                    cur = cur->next;
                }
            }
        }
        return Ans;
    }
};
