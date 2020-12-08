class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(index:int) -> int:
            if arry[index] != index:
                return find(arry[index])
            return arry[index]
        
        def union(a:int, b:int):
            a_root = find(a)
            b_root = find(b)
            if a_root == b_root:
                return
            arry[a_root] = b_root
            self.cnt -= 1
            return
        
        self.cnt = len(stones) #island number
            
        arry = [ i for i in range(len(stones))]
        for a in range(len(stones)):
            for b in range(a+1, len(stones)):
                if stones[a][0] == stones[b][0] or stones[a][1] == stones[b][1]:
                    union(a,b)
                    
        return len(stones) - self.cnt  
