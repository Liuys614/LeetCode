class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def Find(index:int):
            if arry[index] != index:
                root = Find(arry[index])
                return root 
            return arry[index]

        def Union(a:int,b:int):
            a_root = Find(a)
            b_root = Find(b)
            if a_root == b_root: return
            arry[a_root] = b_root
            self.cnt -= 1

        row = len(grid)
        col = len(grid[0])
        arry = [i+j*col if grid[j][i]=="1" else -1 for j in range(row) for i in range(col)]
        self.cnt = sum(grid[j][i]=="1" for i in range(col) for j in range(row)) 
                    
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                index = i + j*col
                if grid[j][i] == "0":
                    continue
                if j>0 and grid[j-1][i] == "1":
                    Union(index,index-col)
                if i>0 and grid[j][i-1] == "1":
                    Union(index, index-1)
                    
        return self.cnt 
