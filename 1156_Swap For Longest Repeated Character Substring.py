
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        gp =[ (i,len(list(v))) for i, v in groupby(text)]
        ct = Counter(text)
        res = 0
        for ch, l in gp:
            res = max(res, min(l+1, ct[ch]))
        
        for i in range(1,len(gp)-1):
            if gp[i-1][0] == gp[i+1][0] and gp[i][1] == 1:
                res = max(res, min(gp[i-1][1] + gp[i+1][1]+1, ct[gp[i-1][0]]))
        return res


