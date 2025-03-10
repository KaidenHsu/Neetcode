using namespace std;
# include <vector>
# include <string>

// Definition for a Pair
class Pair {
public:
    int key;
    string value;

    Pair(int key, string value) : key(key), value(value) {}
};

class Solution {
    public:
        vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
            vector<vector<Pair>> res;
    
            for (int i = 0; i < pairs.size(); i++) {
                Pair hold = pairs[i];
    
                int j;
                for (j = i-1; j >= 0 && pairs[j].key > hold.key; j--) {
                    pairs[j+1] = pairs[j];
                }        
                pairs[j+1] = hold;
    
                res.push_back(pairs);
            }
    
            return res;
        }
};
    