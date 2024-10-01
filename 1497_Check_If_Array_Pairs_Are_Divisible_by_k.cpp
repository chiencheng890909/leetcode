class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        int Len = arr.size();
        int *temp = new int[k + 1](); 
        for(auto it = arr.begin(); it != arr.end(); it++) {
            if(*it < 0)
                *it = abs(*it) % k;
            else if(*it % k == 0)
                *it = 0;
            else
                *it = k - (*it % k);
            temp[*it % k]++;
        }
        
        if(temp[0] % 2 != 0)
            return false;
            
        for(int i = 1; i < int(ceil(k / 2.0)); i++) {
            if(temp[i] != temp[k - i])
                return false;
        }
        return true;
    }
};
