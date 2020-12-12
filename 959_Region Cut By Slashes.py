class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        # initialize union finde array (1-left, 2-right ...)
        self.uf = [ i for i in range(2*N*N)]
        self.cnt = N*N*2
        
        #for each small square union left and right part
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                cur = i+j*N
                if grid[j][i] == " ":
                    self.union(cur*2, cur*2+1)
                if j>0:
                    u = (cur-N)*2+1 if grid[j-1][i]=="/" else (cur-N)*2 
                    d = cur*2+1 if grid[j][i]=="\\" else cur*2 
                    self.union(u,d)
                if i>0:
                    self.union(cur*2, (cur-1)*2+1)
                    
        return self.cnt
                    
        
    def find(self, a:int):
        if self.uf[a]!=a:
            A = self.find(self.uf[a])
            self.uf[a] = A
        return self.uf[a]
        
    def union(self, a:int, b:int):
        A, B = self.find(a), self.find(b)
        if A == B:
            return 
        self.cnt -= 1
        self.uf[A] = B
