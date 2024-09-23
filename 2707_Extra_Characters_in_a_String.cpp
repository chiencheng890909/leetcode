
class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        set<string>wordSet(dictionary.begin(), dictionary.end());
        int n = s.length();
        vector<int> dp(n + 1, 0);
        
        for (int i = n - 1; i > -1; i--) {
            dp[i] = dp[i + 1] + 1;
            for(int length = 1; length < n - i + 1; length++) {
                if (wordSet.find(s.substr(i, length)) != wordSet.end())
                    dp[i] = min(dp[i], dp[i + length]);
            }
        }
        return dp[0];
    }
};
