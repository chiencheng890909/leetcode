class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        stack<int> temp;
        int Ans = 0, Len = target.size();
        int Top;

        temp.push(target[0]);
        for(int i = 1; i < Len; i++) {

            if(target[i] > temp.top()) {
                temp.push(target[i]);
                continue;
            }

            if(target[i] == temp.top()) 
                continue;

            Top = temp.top();

            while(!temp.empty() && target[i] < temp.top()) 
                temp.pop();
            
            Ans += Top - target[i];
            temp.push(target[i]);
        }
        
        if(!temp.empty())
            Ans += temp.top();

        return Ans;
    }
};
