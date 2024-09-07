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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:

public:
    bool DFS(ListNode* head, TreeNode* root) {
        if (head == nullptr)
            return true;
        if (root == nullptr)
            return false;
        // cout << head->val << " " << root->val << endl;

        if (head->val == root->val)
            if(DFS(head->next, root->left) || DFS(head->next, root->right))
                return true;
        return false;
    }

    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root)
            return false;
        return (this->DFS(head, root)) || this->isSubPath(head, root->left) || this->isSubPath(head, root->right);
    }
};
