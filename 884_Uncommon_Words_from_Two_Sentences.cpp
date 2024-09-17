class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        set<string> S1, S2, S1_not, S2_not, Ans_1, Ans_2, Ans;
        string s;

        stringstream s_input_1(s1);
        while (getline(s_input_1, s, ' ')) {
            if(S1.find(s) != S1.end())
                S1_not.insert(s);
            else
                S1.insert(s);
        }

        stringstream s_input_2(s2);
        while (getline(s_input_2, s, ' ')) {
            if(S2.find(s) != S2.end())
                S2_not.insert(s);
            else
                S2.insert(s);
        }

        set_difference(begin(S1), end(S1), begin(S2), end(S2), inserter(Ans_1, begin(Ans_1)));
        set_difference(begin(S2), end(S2), begin(S1), end(S1), inserter(Ans_2, begin(Ans_2)));

        set_difference(begin(Ans_1), end(Ans_1), begin(S1_not), end(S1_not), inserter(Ans, begin(Ans)));
        set_difference(begin(Ans_2), end(Ans_2), begin(S2_not), end(S2_not), inserter(Ans, begin(Ans)));
        return vector<string> (Ans.begin(), Ans.end());
    }
};
