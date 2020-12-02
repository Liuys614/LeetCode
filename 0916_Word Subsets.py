class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # construct set-b which is super set for all strings of B {"char":count...}
        b = {} 
        for s in B:
            tmp = {}
            for c in s:
                if c in tmp:
                    tmp[c] += 1
                else:
                    tmp[c] = 1
                if c in b:
                    b[c] = max(b[c], tmp[c])
                else:
                    b[c] = tmp[c]
                    
        # count number of each character in A and check if containing set-b or not
        res = []
        for s in A:
            tmp = {}
            for c in s:
                tmp[c] = tmp[c] + 1 if c in tmp else 1
                
            check = True
            for c in b:
                if (c not in tmp) or (c in tmp and tmp[c]<b[c]):
                    check = False
            if check:
                res += [s]
        
        return res
