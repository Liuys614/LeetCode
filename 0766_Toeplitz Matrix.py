class Solution:
    pre=[]
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in matrix:
            if not self.check(row):
                return False
        return True
    
    def check(self, row:List[int]) -> bool:
        if not self.pre:
            self.pre = row
            return True
        
        if row[1:] != self.pre[:-1]:
            return False
        
        self.pre = row
        return True


