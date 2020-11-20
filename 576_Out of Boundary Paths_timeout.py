class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        pos = deque()
        pos.append(((j,i),0))
        cnt = 0
        while pos:
            cor, times = pos.popleft()
            if times >= N:
                continue
            neighbor = [(cor[0]-1,cor[1]),(cor[0]+1,cor[1]),(cor[0],cor[1]-1),(cor[0],cor[1]+1)]
            for next in neighbor:
                if next[0]==-1 or next[0]==n or next[1]==-1 or next[1]==m:
                    cnt +=1
                elif times + 1 < N:
                    pos.append((next,times+1))
        return cnt 
        
