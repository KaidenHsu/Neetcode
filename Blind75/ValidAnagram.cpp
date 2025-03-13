using namespace std;
#include <string>
#include <map>

class Solution {
    public:
        bool isAnagram(string s, string t) {
            map<char, int> mp1 = {};
            map<char, int> mp2 = {};
    
            for (char c: s) {
                if (mp1.find(c) != mp1.end()) {
                    mp1[c]++;
                } else {
                    mp1.insert({c, 1});
                }
            }
    
            for (char c: t) {
                if (mp2.find(c) != mp2.end()) {
                    mp2[c]++;
                } else {
                    mp2.insert({c, 1});
                }
            }
    
            if (mp1 == mp2) {
                return true;
            }
    
            return false;
        }
    };