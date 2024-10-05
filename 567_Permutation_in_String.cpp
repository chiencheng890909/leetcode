class Solution {
public:
    array<int, 26> count(string& str, int start, int end) {
        array<int, 26> freq = {0};
        for(int i = start; i < end; i++) 
            freq[str[i] - 'a'] ++;
        return freq;
    }
    bool checkInclusion(string s1, string s2) {
        int Len_1 = s1.length();
        int Len_2 = s2.length();
        if(Len_1 > Len_2)
            return false;
            
        array<int, 26> freq_1 = count(s1, 0, Len_1);
        array<int, 26> freq_2 = count(s2, 0, Len_1);
        for(int i = 0; i < Len_2 - Len_1; i++) {
            if(freq_1 == freq_2)
                return true;
            else {
                freq_2[s2[i] - 'a']--;
                freq_2[s2[i + Len_1] - 'a']++;
            }
        }
        if(freq_1 == freq_2)
            return true;
        return false;
    }
};
