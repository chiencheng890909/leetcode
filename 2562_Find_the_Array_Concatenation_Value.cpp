class Solution {
public:
    long long findTheArrayConcVal(vector<int>& nums) {
        int index = 0;
        int Len = nums.size();
        int stop = Len / 2;
        long long Ans = 0;

        while(index < stop) {
            Ans += stoll(to_string(nums[index]) + to_string(nums[Len - index - 1]));
            index++;
        }
        if(Len % 2 != 0)
            Ans += nums[index];

        return Ans;
    }
};
