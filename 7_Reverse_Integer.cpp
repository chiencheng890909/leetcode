class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x != 0) {
            if (x == INT_MAX || x == INT_MIN)
                return 0;
            else if (x < 0) {
                if ((INT_MIN + (-x % 10)) / 10 > ans)
                    return 0;
                ans = ans * 10 - (-x) % 10;
            }
            else {
                if ((INT_MAX - x % 10) / 10 < ans)
                    return 0;
                ans = ans * 10 + (x % 10);
            }
            x /= 10;
        }
        return ans;
    }
};
