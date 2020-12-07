class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        maxGrid=[[ 0 for i in range(len(grid[0]))] for j in range(len(grid))]
        minGrid=[[ 0 for i in range(len(grid[0]))] for j in range(len(grid))]
        m = 10**9 + 7 
        for j, r in enumerate(grid):
            for i, c in enumerate(r):
                if i==0 and j == 0:
                    maxGrid[j][i]=grid[j][i]
                    minGrid[j][i]=grid[j][i]
                    continue
                if i==0:
                    maxGrid[j][i] = grid[j][i]*maxGrid[j-1][i]
                    minGrid[j][i] = grid[j][i]*minGrid[j-1][i]
                    continue
                if j==0:
                    maxGrid[j][i] = grid[j][i]*maxGrid[j][i-1]
                    minGrid[j][i] = grid[j][i]*minGrid[j][i-1]
                    continue
                    
                maxGrid[j][i] = max(grid[j][i]*maxGrid[j-1][i], 
                                    grid[j][i]*maxGrid[j][i-1], 
                                    grid[j][i]*minGrid[j-1][i], 
                                    grid[j][i]*minGrid[j][i-1],)
                
                minGrid[j][i] = min(grid[j][i]*maxGrid[j-1][i], 
                                    grid[j][i]*maxGrid[j][i-1], 
                                    grid[j][i]*minGrid[j-1][i], 
                                    grid[j][i]*minGrid[j][i-1],)
                
        res = maxGrid[len(grid)-1][len(grid[0])-1]
        return res%m if res >=0 else -1 
