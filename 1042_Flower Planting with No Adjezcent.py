class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0 for _ in range(n+1)]       #[garden]=color
        nei = {i:set() for i in range(n+1)} #garden:{neighbor}
        for x,y in paths:
            nei[x].add(y) 
            nei[y].add(x) 
            
        for i in range(1,n+1):
            used = {res[j] for j in nei[i]}
            colors = {1,2,3,4} - used
            res[i] = colors.pop()           #chose the first one
            
        return res[1:] 
