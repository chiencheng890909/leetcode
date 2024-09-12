class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int Ans = 0;
        set<char> Allow(allowed.begin(), allowed.end());
        
        set<char> Words;
        set<char> intersection;

        for(int i = 0; i < words.size(); i++) {
            set<char> Words(words[i].begin(), words[i].end());
            intersection.clear();
            set_intersection(Words.begin(), Words.end(), Allow.begin(), Allow.end(), inserter(intersection, intersection.begin()));
            if(intersection == Words)
                Ans++;
        }
        return Ans;
    }
};
