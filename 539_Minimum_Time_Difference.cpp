class Solution {
public:
    int Time_diff(string time_1, string time_2) {
        int time_1_h = stoi(time_1.substr(0, 2));
        int time_1_m = stoi(time_1.substr(3, 2));
        int time_2_h = stoi(time_2.substr(0, 2));
        int time_2_m = stoi(time_2.substr(3, 2));

        int ans = abs((time_1_h - time_2_h) * 60 + (time_1_m - time_2_m));
        return min(ans, 1440 - ans);
    }
    int findMinDifference(vector<string>& timePoints) {
        int Len = timePoints.size();
        sort(timePoints.begin(), timePoints.end());
        int ans = 1440; 
        for(int i = 0; i < Len - 1; i++) {
            ans = min(ans, Time_diff(timePoints[i], timePoints[i + 1]));
            if (ans == 0)
                return 0;
        }
        ans = min(ans, Time_diff(timePoints[0], timePoints[Len - 1]));

        return ans;
    }
};
