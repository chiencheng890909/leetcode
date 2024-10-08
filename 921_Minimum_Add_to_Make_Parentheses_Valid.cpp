class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char> temp;
        int Len = s.length();
        temp.push(s[0]);
        for(int i = 1; i < Len; i++) {
            if(!temp.empty() && temp.top() == '(' && s[i] == ')')
                temp.pop();
            else
                temp.push(s[i]);
        }
        return temp.size();
    }
};
