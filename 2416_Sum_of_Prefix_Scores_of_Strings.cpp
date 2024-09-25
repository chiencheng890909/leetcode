struct Node {
    map<char, Node> children;
    int num = 1;
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
                currentNode->num ++;
            }
            else {
                Node* temp = new Node();
                currentNode->children[c] = *temp;
                currentNode = &currentNode->children[c];
            }
        }
    }
    int search(string word) {
        Node *currentNode = &root;
        char c;
        int Ans = 0;
        map<char, Node>::iterator iter;
        for (int i = 0; i < word.length(); i++) {
            c = word[i];
            if (currentNode->children.find(c) != currentNode->children.end()) {
                currentNode = &currentNode->children[c];
                Ans += currentNode->num;
            }
            else 
                return Ans;
        }
        return Ans;
    }
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        int Size = words.size();
        vector<int> Ans(Size, 0);
        Trie Tree;
        for(int i = 0; i < Size; i++) {
            Tree.insert(words[i]);
        }
        for(int i = 0; i < Size; i++) {
            Ans[i] = Tree.search(words[i]);
        }
        return Ans;
    }
};
