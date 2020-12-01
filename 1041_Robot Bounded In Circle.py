
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        l, r, x, y, dir = 0, 0, 0, 0, 0
        for v in instructions:
            if v == "L":
                l+=1
                dir=(dir+3)%4
            if v == "R":
                r+=1
                dir=(dir+1)%4
            if v == "G":
                x += dirs[dir][0]
                y += dirs[dir][1]

        dirSum = abs(l-r) % 4
        return True if dirSum != 0 or (x,y) == (0,0) else False
