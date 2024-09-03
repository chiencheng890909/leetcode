class Solution {
public:
    int getLucky(string s, int k) {
        int num = 0;
        for(int i = 0; i < s.size(); i++) {
            int char_int = (int(s[i]) - int('a') + 1);
            num += (char_int / 10 + char_int % 10);
        }
        int Ans = num;
        while (k > 1) {
            Ans = 0;
            while (num > 0) {
                Ans += (num % 10);
                num /= 10;
            }
            num = Ans; 
            k -= 1;
        }
        return Ans;
    }
};