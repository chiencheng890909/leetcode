class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int p_size = patterns.size();
        int ans = 0;
        for(int i = 0; i < p_size; i++) {
            if(word.find(patterns[i]) != std::string::npos) 
                ans++;
        }
        return ans;
    }
};
