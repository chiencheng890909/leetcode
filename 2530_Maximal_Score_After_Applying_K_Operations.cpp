class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue <int> n(nums.begin(), nums.end());
        long long ans = 0;
        int temp;
        for(int i = 0; i < k; i++) {
            temp = n.top();
            ans += temp;
            n.pop();
            n.push(ceil(temp / 3.0));
        }
        return ans;
    }
};
