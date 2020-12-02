class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        avg = total//3
        part, cnt = 0, 0
        
        if total%3 != 0: return False
        
        for v in A[:-1]:
            part += v
            if part == avg:
                cnt += 1
                part = 0
                
        return True if cnt >= 2 else False
