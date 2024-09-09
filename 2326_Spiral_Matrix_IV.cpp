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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> ans(m, vector<int>(n, -1));
        int i = 0; // m
        int j = 0; // n
        int gap = 1;
        int circle = 0;
        int next_i;
        int next_j;
        while(head != nullptr) {
            ans[i][j] = head->val;
            next_i = i + gap;
            next_j = j + gap;

            if (circle <= next_j && next_j < n - circle )
                j = next_j;
            else if (circle < next_i && next_i < m - circle)
                i = next_i;
            else {
                if (i == circle + 1 && j == circle)
                    circle ++;
                gap = -(gap);
                j += gap;
            }
            head = head->next;
        }
        return ans;
    }
};
