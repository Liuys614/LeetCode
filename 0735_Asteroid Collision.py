class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        r = list(reversed(asteroids))
        l = list()
        
        while r:
            L = l.pop() if l else None
            R = r.pop() if r else None
            
            if not L:
                l.append(R) 
                continue
            elif (L<0 and R<0) or (L<0 and R>0) or (L>0 and R>0):
                l.append(L)
                l.append(R)
                continue
            else:    
                if abs(R) == abs(L):
                    continue
                elif abs(R) > abs(L):
                    r.append(R)
                    continue
                elif abs(R) < abs(L):
                    l.append(L)
                    continue

        return l
