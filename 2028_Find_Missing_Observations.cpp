class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int Value = (m + n) * mean;
        Value = Value - accumulate(rolls.begin(), rolls.end(), 0);
        if (Value > n * 6 || Value < n)
            return {};
        div_t q_r = div(Value, n);
        vector<int> ans(n, q_r.quot);
        fill(ans.begin(), ans.begin() + q_r.rem, q_r.quot + 1);
        return ans;
    }
};