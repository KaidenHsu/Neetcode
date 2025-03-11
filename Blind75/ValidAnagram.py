class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Tip: First consider length
        if len(s) != len(t):
            return False
        
        set_s, set_t = {}, {}

        for char in s:
            if char in set_s:
                set_s[char] += 1
            else:
                set_s[char] = 1
            
        for char in t:
            if char in set_t:
                set_t[char] += 1
            else:
                set_t[char] = 1

        if set_s == set_t:
            return True
        else:
            return False