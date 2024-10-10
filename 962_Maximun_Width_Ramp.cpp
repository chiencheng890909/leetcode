class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        stack<int> temp;
        int Ans = 0, len = nums.size();
        for(int i = 0; i < len; i++)
            if(temp.empty() || nums[temp.top()] > nums[i])
                temp.push(i);
        for(int i = len - 1; i >= 0; i--) {
            while(!temp.empty() && nums[temp.top()] <= nums[i]) {
                Ans = max(i - temp.top(), Ans);
                temp.pop();
            }
        }
        return Ans;
    }
};