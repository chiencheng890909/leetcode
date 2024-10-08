class Solution {
public:
    int minSwaps(string s) {
        stack<char> temp;
        temp.push(s[0]);
        for(int i = 1; i < s.length(); i++) {
            if(!temp.empty() && (s[i] == ']' && temp.top() == '[')) 
                temp.pop();
            else
                temp.push(s[i]);
        }
        return (temp.size() / 2 + 1) / 2;
    }
};
