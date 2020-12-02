class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = ceil(len(b)/len(a))
        for i in range(n, n+2)  :
            if b in a * i : 
                return i 
            
        return -1 
