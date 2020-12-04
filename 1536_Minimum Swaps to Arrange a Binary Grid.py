class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # calculate continue 0s from right
        right0 = []
        for r in grid:
            cnt = 0
            for c in reversed(r):
                if c == 0: 
                    cnt += 1
                else:
                    break
            right0.append(cnt)
        
        # check valid
        tmp = right0.copy()
        tmp.sort(reverse=True)
        for i, v in enumerate(tmp):
            if v < len(tmp)-1-i:
                return -1 
            
        # try swap
        res = 0
        for i, v in enumerate(right0):
            if v < len(right0)-1-i:
                for j, v in enumerate(right0[i+1:]):
                    if v >= len(right0)-1-i:
                        r = right0[i+j+1]
                        del right0[i+j+1]
                        right0.insert(i,r)
                        res += j+1 
                        break
        
        return res
