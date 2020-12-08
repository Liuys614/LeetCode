class Solution:
    
    def explore(self, j:int, i:int, grid:List[List[str]]):
        if j < 0 or j >= len(grid) or i<0 or i>=len(grid[0]) or grid[j][i] != "1":
            return
        grid[j][i]= "x" 
        self.explore(j-1,i,grid)
        self.explore(j,i-1,grid)
        self.explore(j+1,i,grid)
        self.explore(j,i+1,grid)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = []
        cnt = 0 
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == "1":
                    cnt+=1
                    self.explore(j,i,grid) 
        return cnt
