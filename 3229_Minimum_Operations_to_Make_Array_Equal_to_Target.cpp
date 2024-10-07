class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        int Len = target.size();
        for(int i = 0; i< Len; i++) 
            target[i] -= nums[i];
        
        stack<int> temp;
        long long Ans = 0;
        int Top;
        temp.push(target[0]);

        for(int i = 1; i < Len; i++) {
            if((target[i] > 0 && temp.top() < 0) || (target[i] < 0 && temp.top() > 0)) {
                Top = temp.top();
                if(Top > 0) {
                    while(!temp.empty() && temp.top() > 0) 
                        temp.pop();
                }
                else {
                    while(!temp.empty() && temp.top() < 0) 
                        temp.pop();
                }
                temp.push(target[i]);
                Ans += abs(Top);
                continue;
            }
            else {
                 if(abs(target[i]) > abs(temp.top())) {
                    temp.push(target[i]);
                    continue;
                }

                if(target[i] == temp.top()) 
                    continue;

                Top = temp.top();
                while(!temp.empty() && abs(target[i]) < abs(temp.top())) 
                    temp.pop();
                Ans += abs(Top - target[i]);
                temp.push(target[i]);
            }
        }
        if(!temp.empty())
            Ans += abs(temp.top());

        return Ans;
    }
};
