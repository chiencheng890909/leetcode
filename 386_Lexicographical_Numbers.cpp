bool comparison(int A, int B) {
    if (to_string(A) > to_string(B))
        return false;
    else
        return true;
}
class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> Ans(n);
        for(int i = 0; i < n; i++)
            Ans[i] = i + 1;

        sort(Ans.begin(), Ans.end(), comparison);
        return Ans;
    }
};
