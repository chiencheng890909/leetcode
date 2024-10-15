class Solution {
public:
    long long minimumSteps(string s) {
        int len = s.length();
        int zero_loc = 0;
        long long ans = 0;
        for(int i = 0; i < len; i++) {
            if(s[i] == '0') {
                ans += i - zero_loc;
                zero_loc++;
            }
        }
        return ans;
    }    
};
