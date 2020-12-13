#DFS
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        def dfs(u:int):
            for v,w in dic[u]:
                new =  df[u] + w
                if new < df[v]:
                    df[v] = new 
                    dfs(v)
        
        df = [math.inf if i!=K else 0 for i in range(N+1)]
        dic = [[] for i in range(N+1)]
        for u,v,w in times:
            dic[u].append((v,w))
                
        dfs(K)
        return max(df[1:]) if all([ v != math.inf for v in df[1:]]) else -1

#Dijastra
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        df = [math.inf for i in range(N+1)]
        dic = [[] for i in range(N+1)]
        heap = [(0,K)]
            
        for u,v,w in times:
            dic[u].append((v,w))
                
        while heap:
            time, node = heapq.heappop(heap)
            if time < df[node] :
                df[node] = time
                for v, w in dic[node]:
                    heapq.heappush(heap,(time+w,v))
            
        res = max(df[1:])
        return res if res < math.inf else -1

#Bellman Ford
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        df = [math.inf if i != K else 0 for i in range(N+1)]
                
        for _ in range(N-1):
            change = False
            for u,v,w in times:
                df[v] = min(df[u]+w, df[v])
                change = True
            if not change: # if no change, means it's optimized
                break
            
        res = max(df[1:])
        return res if res < math.inf else -1
