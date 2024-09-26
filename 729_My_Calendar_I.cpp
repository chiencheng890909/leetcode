class MyCalendar {
private:
    vector<int*> Calendar;
public:
    MyCalendar() {
        
    }
    bool book(int start, int end) {
        int len = Calendar.size();
        for(int i = 0; i < len; i++) 
            if(this->Calendar[i][0] < end && this->Calendar[i][1] > start)
                return false;
        int *temp = new int [2];
        temp[0] = start;
        temp[1] = end;
        this->Calendar.push_back(temp);
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
