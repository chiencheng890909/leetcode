struct Node {
    int val = 0;
    Node *next = nullptr;
    Node *prev = nullptr;
};
 

class CustomStack {
private:
    Node * Head;
    Node * Tail;
    int Size;
    int Max_Size;
public:
    CustomStack(int maxSize) {
        Head = new Node();
        Tail = Head;
        Max_Size = maxSize;
        Size = 0;
    }
    
    void push(int x) {
        if(Size < Max_Size) {
            Node* add = new Node();

            add->prev = Tail;
            add->val = x;
            Tail->next = add;
            Tail = add;
            Size++;
        }
    }
    
    int pop() {
        if(Size > 0) {
            Node* Del = Tail;
            int temp = Del->val;
            Tail = Tail->prev;
            Tail->next = nullptr;
            delete Del;
            Size--;
            return temp;
        }
        else
            return -1;
    }
    
    void increment(int k, int val) {
        Node* it = Head->next;
        for(int i = 0; i < k; i++) {
            if(it == nullptr)
                break;
            else {
                it->val = it->val + val;
                it = it->next;
            }
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
