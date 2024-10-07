class Solution {
public:
    int minLength(string s) {
        string::size_type AB, CD;
        AB = s.find("AB");
        CD = s.find("CD");
        while(AB != s.npos || CD != s.npos) {
            if(AB != s.npos) {
                s.replace(AB, 2, "");
                AB = s.find("AB");
                CD = s.find("CD");
            }

            if(CD != s.npos) {
                s.replace(CD, 2, "");
                AB = s.find("AB");
                CD = s.find("CD");
            }
        }
        return s.length();
    }
};
