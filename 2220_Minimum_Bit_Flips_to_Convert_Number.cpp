class Solution {
public:
    string Flip(int num) {
        string ans;
        while(num != 0) {
            ans += (char('0' + num % 2));
            num /= 2;
        }
        return ans;
    }
    int minBitFlips(int start, int goal) {
        string str_1 = Flip(start);
        string str_2 = Flip(goal);
        while (str_1.size() != str_2.size()) {
            if(str_1.size() > str_2.size())    
                str_2 += "0";
            else if(str_1.size() < str_2.size()) 
                str_1 += "0";
        }
        int ans = 0;
        int Len = str_1.size();
        for(int i = 0; i < Len; i++) {
            if (str_1[i] != str_2[i])
                ans ++;
        }
        return ans;
    }
};
