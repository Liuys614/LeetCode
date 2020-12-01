class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        dp = {dir:[[1 for i in range(N)] for j in range(N)] for dir in ["left","right","top","down"]}
        
        # mark all cell as 1 and mines as 0
        map = [[1 for i in range(N)] for j in range(N)]
        for pt in mines:
            map[pt[0]][pt[1]] = 0
        
        #calculat distance from left/right/top/down
        l, r, t, d=0, 0, 0, 0
        for j in range(N):
            l, r = 0, 0
            for i in range(N):
                l = 0 if map[j][i] == 0 else l+1
                r = 0 if map[j][N-i-1] == 0 else r+1
                dp["left"][j][i] = l
                dp["right"][j][N-i-1] = r

        for i in range(N):
            t, d = 0, 0
            for j in range(N):
                t = 0 if map[j][i] == 0 else t+1
                d = 0 if map[N-j-1][i] == 0 else d+1
                dp["top"][j][i] = t
                dp["down"][N-j-1][i] = d
                
        #get the bigest plus with the cell on the center
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, min([dp[dir][j][i] for dir in dp]))
                          
        return res
