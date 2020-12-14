class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connect = [set() for _ in range(n)]
        res=0
            
        for a,b in roads:
            connect[a].add(b)
            connect[b].add(a)
            
        for i in range(n):
            for j in range(i+1,n):
                res = max(res, len(connect[i])+len(connect[j])-(1 if i in connect[j] else 0) )
            
        return res 
