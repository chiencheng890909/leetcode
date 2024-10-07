class Solution {
public:
    bool canConstruct(string s, int k) {
        if(k == s.length())
            return true;
        if(k > s.length())
            return false;

        map<char, int> dict;

        for(auto c:s) 
            dict[c] ++;
            
        int Times = 0;
        for (auto it = dict.begin(); it != dict.end(); ++it) {
            if(it->second % 2 == 1)
                Times++;
        }
        return Times <= k;
    }
};
