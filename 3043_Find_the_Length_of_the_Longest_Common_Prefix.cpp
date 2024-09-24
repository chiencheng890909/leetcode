struct Node {
    map<char, Node> children;
};

class Trie {
private:
    Node root;
public:
    void insert(string word) {
        Node *currentNode = &root;
        char c;
        for (int i = 0; i < word.length(); i++) {
            c = word[i];
            if (currentNode->children.find(c) != currentNode->children.end()) {
                currentNode = &currentNode->children[c];
                // cout << "find " << c << endl;
            }
            else {
                Node* temp = new Node();
                currentNode->children[c] = *temp;
                currentNode = &currentNode->children[c];
                // cout << "add " << c << endl;
            }
        }
        cout << endl;
    }
    int search(string word) {
        Node *currentNode = &root;
        char c;
        int Ans = 0;
        map<char, Node>::iterator iter;
        for (int i = 0; i < word.length(); i++) {
            c = word[i];
            if (currentNode->children.find(c) != currentNode->children.end()) {
                // cout << "count " << c << endl;
                currentNode = &currentNode->children[c];
                Ans++;
            }
            else 
                break;
        }
        // cout << endl;
        return Ans;
    }
};

class Solution {
public:
    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        Trie dic_1, dic_2;
        int Size_1 = arr1.size();
        int Size_2 = arr2.size();
        int Ans = 0;

        for(int i = 0; i < Size_1; i++) 
            dic_1.insert(to_string(arr1[i]));

        for(int j = 0; j < Size_2; j++) 
            Ans = max(Ans, dic_1.search(to_string(arr2[j])));

        for(int j = 0; j < Size_2; j++) 
            dic_2.insert(to_string(arr2[j]));
        
        for(int i = 0; i < Size_1; i++) 
            Ans = max(Ans, dic_2.search(to_string(arr1[i])));


        return Ans;
    }
};
