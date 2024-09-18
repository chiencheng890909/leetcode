bool compare(int A, int B) {
    string S_A = to_string(A);
    string S_B = to_string(B);

    if (S_A + S_B > S_B + S_A)
        return true;
    else
        return false;
}

class Solution {
public:
    
    string largestNumber(vector<int>& nums) {
        string Ans;
        int Len = nums.size();
        
        sort(nums.begin(), nums.end(), compare);

        if(nums[0] == 0)
            return "0";

        for (int i = 0; i < Len; i++) 
            Ans += to_string(nums[i]);
        return Ans;
    }
};
