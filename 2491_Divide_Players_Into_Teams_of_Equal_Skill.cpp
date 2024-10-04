class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int Len = skill.size();
        long long Sum = skill[0] + skill[Len - 1];
        long long Ans = skill[0] * skill[Len - 1];
        for(int i = 1; i < Len / 2; i++) {
            if(Sum != (skill[i] + skill[Len - i - 1]))
                return -1;
            Ans += (skill[i] * skill[Len - i - 1]);
        }
        return Ans;
    }
};
