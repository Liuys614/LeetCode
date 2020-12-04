class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        
        if len(pattern) != len(s):
            return False
        
        d1, d2 = {}, {}
            
        for i, c in enumerate(pattern):
            if c in d1 and d1[c] != s[i]:
                return False
            else:
                d1[c] = s[i]
                
            if s[i] in d2 and d2[s[i]] != c:
                return False
            else:
                d2[s[i]] = c
                
        return True
