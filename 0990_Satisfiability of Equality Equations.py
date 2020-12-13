class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = {}
        def union(a:str, b:str): 
            A, B = find(a), find(b)
            if A != B: uf[A] = B
            
        def find(a:str)->str:
            uf.setdefault(a,a)
            return find(uf[a]) if uf[a]!=a else uf[a]
        
        # union every same value as same union
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1:3]
            if op == "==":
                union(v1, v2)
                
        # check difference between beloning union
        for eq in equations:
            v1, v2, op = eq[0], eq[3], eq[1:3]
            if op == "!=":
                if find(v1) == find(v2):
                    return False
                
        return True
