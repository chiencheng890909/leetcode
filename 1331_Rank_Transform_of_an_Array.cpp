class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int> temp(arr.begin(), arr.end());
        map<int, int> order;
        int Size = 1;
        int Del;
        auto it = temp.begin();
        while(it != temp.end()) {
            Del = *(it);
            order[Del] = Size;
            Size++;
            it++;
        }

        Size = arr.size();
        for(int i = 0; i < Size; i++) 
            arr[i] = order[arr[i]];
        return arr;
    }
};
