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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        ios::sync_with_stdio(false);

        set<int> st(nums.begin(), nums.end());
        ListNode* Position = head;
        ListNode* Pre = new ListNode(-1, head);
        ListNode* Ans = Pre;

        while (Position != nullptr) {
            if (st.count(Position->val))
                Pre->next = Position->next;
            else 
                Pre = Pre->next;
            Position = Position->next;
        }
        return Ans->next;
    }
};
