class Solution:
    nb = dict() # (mid, {head, tail})
    def makeBeautiful(self, cur:List[int], N:int) -> List[int]:
        if len(cur) == N:
            return cur
        
        if cur[-1] in self.nb:
            for s in self.nb[cur[-1]]:
                if len(s & set(cur)) == 1 :
                    return []
            
        for i in range(1,N+1):
             if i not in cur:
                str = self.makeBeautiful(cur+[i], N)
                if str:
                    return str
        
    def beautifulArray(self, N: int) -> List[int]:
        # find every not beautiful case
        for i in range(1, (N+1)//2):
            for a in range(1,N+1):
                if a + 2*i <= N:
                    if a+i in self.nb:
                        self.nb[a+i].append(set([a,a+2*i]))
                    else:
                        self.nb[a+i]= [set([a,a+2*i])]
        
        # traversal each case until find one
        for i in range(1,N+1):
            str = self.makeBeautiful([i], N)
            if str:
                return str
