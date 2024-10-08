bool comparison(char A, char B) {
    if(A > B)
        return true;
    else
        return false;
}

class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        vector<string> ans;
        string str, pre;
        int len = words.size();
        for(int i = 0; i < len; i++) {
            str = words[i];
            sort(str.begin(), str.end(), comparison);
            if(str != pre) 
                ans.push_back(words[i]);
            pre = str;
        }
        return ans;
    }
};
