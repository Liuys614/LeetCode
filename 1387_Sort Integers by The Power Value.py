class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.cache = {} #num:powers
        res = [] 
        for i in range(lo, hi+1):
            res.append((i,self.getPower(i)))
            
        res.sort(key= lambda x : x[1])
        return res[k-1][0]
        
    def getPower(self, n:int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return 0 
        if n%2:
            m = n*3+1
        else:
            m = n//2
        self.cache.setdefault(m, self.getPower(m))
        self.cache.setdefault(n, self.cache[m]+1)
        return self.cache[n]
