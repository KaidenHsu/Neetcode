using namespace std;
#include <vector>
#include <set>

class Solution {
    public:
        bool hasDuplicate(vector<int>& nums) {
            set<int> s = {};
    
            for (int num: nums) {
                if (s.find(num) != s.end()) { // num in nums
                    return true;
                }
    
                s.insert(num);
            }
    
            return false;
        }
    };