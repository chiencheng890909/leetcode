class Solution {
private:
    set<string> ans;
    map<char, int> choices;
public:
    void Backtracking(string sub) {
        for (auto it = choices.begin(); it != choices.end(); ++it) {
            if(it->second > 0) {
                it->second--;
                sub.push_back(it->first);

                ans.insert(sub);
                Backtracking(sub);

                sub.pop_back();
                it->second++;
            }
        }
    }
    int numTilePossibilities(string tiles) {
        for(auto it = tiles.begin(); it < tiles.end(); it++) {
            if(choices.contains(*it))
                choices[*it] ++;
            else
                choices[*it] = 1;
        }
        Backtracking("");
        return ans.size();
    }
};
