class MyCircularDeque {
private:
    deque<int> Contain;
    int Max_Size;
    int Size;
public:
    MyCircularDeque(int k) {
        Size = 0;
        Max_Size = k;
    }
    
    bool insertFront(int value) {
        if(Size < Max_Size) {
            Contain.push_front(value);
            Size++;
            return true;
        }
        return false;
    }
    
    bool insertLast(int value) {
        if(Size < Max_Size) {
            Contain.push_back(value);
            Size++;
            return true;
        }
        return false;
    }
    
    bool deleteFront() {
        if(Size > 0) {
            Contain.pop_front();
            Size--;
            return true;
        }
        return false;
    }
    
    bool deleteLast() {
        if(Size > 0) {
            Contain.pop_back();
            Size--;
            return true;
        }
        return false;
    }
    
    int getFront() {
        if(Size > 0) 
            return Contain.front();
        return -1;
    }
    
    int getRear() {
        if(Size > 0) 
            return Contain.back();
        return -1;
    }
    
    bool isEmpty() {
        if(Size > 0) 
            return false;
        else
            return true;
    }
    
    bool isFull() {
        if(Size == Max_Size) 
            return true;
        else
            return false;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
