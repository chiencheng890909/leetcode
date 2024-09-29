class AllOne {
private:
    map<string, int> Dic;
    map<string, int>::iterator Min_it;
    map<string, int>::iterator Max_it;
    int Size;
public:
    AllOne() {
        Size = 0;
        Min_it = Dic.end();
        Max_it = Dic.end();
    }

    void inc(string key) {
        if (Dic.contains(key)) {
            Dic[key] += 1;
        }
        else {
            Dic[key] = 1;
            Size += 1;
        }
        Min_it = Dic.end();
        Max_it = Dic.end();
    }
    
    void dec(string key) {
        if (Dic[key] == 1) {
            Dic.erase(key);
            Size -= 1;
        }
        else {
            Dic[key] -= 1;
        }
        Min_it = Dic.end();
        Max_it = Dic.end();
    }
    
    string getMaxKey() {
        if(Size > 0) {
            if(Max_it == Dic.end()) {
                Max_it = Dic.begin();
                for(auto it = Dic.begin(); it != Dic.end(); it ++) {
                    if((*Max_it).second < (*it).second)
                        Max_it = it;
                }
            }
            return (*Max_it).first;
        }
        else
            return "";
    }
    
    string getMinKey() {
        if(Size > 0) {
            if(Min_it == Dic.end()) {
                Min_it = Dic.begin();
                for(auto it = Dic.begin(); it != Dic.end(); it ++) {
                    if((*Min_it).second > (*it).second)
                        Min_it = it;
                }
            }
            return (*Min_it).first;
        }
        else
            return "";
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */
