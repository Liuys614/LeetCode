class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = [(i, self.getPower(i)) for i in range(lo, hi+1)] 
        res.sort(key= lambda x : x[1])
        return res[k-1][0]
    
    @lru_cache()   
    def getPower(self, n:int) -> int:
        if n == 1:
            return 0 
        if n%2:
            m = n*3+1
        else:
            m = n//2
        return self.getPower(m)+1
