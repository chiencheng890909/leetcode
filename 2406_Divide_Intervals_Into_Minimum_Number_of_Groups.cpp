class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<int> A, B;
        int len = intervals.size();
        for(int i = 0; i < len; i++) {
            A.push_back(intervals[i][0]);
            B.push_back(intervals[i][1]);
        }
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        
        int i = 0, ans = 0;
        for(auto s:A) {
            if(s > B[i])
                i++;
            else
                ans++;
        }
        return ans;
    }
};