class MyCalendarTwo {
private:
    vector<int*> Calendar;

public:
    MyCalendarTwo() {
        
    }
    bool check(int* temp) {
        int len = this->Calendar.size();
        int start = temp[0];
        int end = temp[1];
        int Times = 0;
        for(int i = 0; i < len; i++) {
            if(this->Calendar[i][0] < end && this->Calendar[i][1] > start) {
                Times++;
                if(Times == 2)
                    return true;
            }
        }
        return false;
    }

    bool book(int start, int end) {
        int len = Calendar.size();
        int* temp;

        for(int i = 0; i < len; i++) {
            if(this->Calendar[i][0] < end && this->Calendar[i][1] > start) {
                temp = new int [2];
                temp[0] = max(start, this->Calendar[i][0]);
                temp[1] = min(end, this->Calendar[i][1]);
                if(check(temp))
                    return false;
            }
        }
        
        temp = new int [2];
        temp[0] = start;
        temp[1] = end;
        this->Calendar.push_back(temp);
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
