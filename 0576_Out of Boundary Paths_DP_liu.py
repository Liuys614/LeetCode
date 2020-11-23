"""
    1. 使用table(dp)紀錄每個格子，走N步可以到達目前位置的可能數
    2. 正著思考，走一步、走兩步....
    3. 用count記得目前走這一步之前得了幾分

    p.s
    - 反著思考可以用一樣的時間複雜度得到所有格子出發的答案
    - 反著思考的意思是，剩一步、剩兩步...從這個格子出發可以得幾分
"""

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        cnt = 0
        dp = [[0 for x in range(n)] for y in range(m)]
        dp[i][j] = 1
        M = 10**9 + 7    
        for step in range(N):
            tmp = [[0 for x in range(n)] for y in range(m)]
            print(dp)
            for y in range(m):
                for x in range(n):
                    if dp[y][x] == 0:
                        continue
                    if x == 0:
                        cnt += dp[y][x]
                    if x == n-1:
                        cnt += dp[y][x]
                    if y == 0:
                        cnt += dp[y][x]
                    if y == m-1:
                        cnt += dp[y][x]
                    if x>0: 
                        tmp[y][x-1] += dp[y][x] 
                    if y>0:
                        tmp[y-1][x] += dp[y][x]
                    if x<n-1:
                        tmp[y][x+1] += dp[y][x]
                    if y<m-1:
                        tmp[y+1][x] += dp[y][x]
            print(cnt) 
            dp = tmp
        return cnt%M




