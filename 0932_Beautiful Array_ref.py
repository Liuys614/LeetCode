class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1:
            return [1]
        
        oddArry = [ i*2-1 for i in self.beautifulArray((N+1)//2)]
        evenArry = [ i*2 for i in self.beautifulArray(N//2)]
        
        return oddArry + evenArry 
