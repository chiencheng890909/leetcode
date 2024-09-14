class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int max = 0;
        int max_length = 0;
        int temp = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) 
            if (*it > max)
                max = *it;
                
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
            if (*it == max) 
                temp ++;
            else 
                temp = 0;

            if (max_length < temp)
                max_length = temp;
        }
        return max_length;
    }
};
