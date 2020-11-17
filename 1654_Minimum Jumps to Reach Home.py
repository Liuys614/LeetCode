"""
    1. 用array來記錄步數
    2. 用deque來紀錄移動歷史(DFS)
    3. 用-1代表不能移動過去的地方
    4. 用inf代表可以去但還沒踏過的地方
    5. 用deque append來實現BFS
"""
import math
import collections
def minimumJumps(forbidden:[int], a: int, b: int, x: int) -> int: 
    max_val = max([x]+forbidden) +a+b
    stepLog = [0]+[math.inf]*max_val # Jump step
    for pos in forbidden:
        stepLog[pos] = -1

    moveQueue = collections.deque([0])

    while moveQueue:
        pos=moveQueue.popleft()

        if pos+a <= max_val and stepLog[pos]+1 < stepLog[pos+a]:
            moveQueue.append(pos+a)
            stepLog[pos+a] = stepLog[pos]+1
        if pos-b > 0 and stepLog[pos]+1 < stepLog[pos-b]:
            stepLog[pos-b] = stepLog[pos]+1
            if pos-b+a<=max_val and stepLog[pos-b+a]>stepLog[pos]+2:
                moveQueue.append(pos-b+a)
                stepLog[pos-b+a]=stepLog[pos]+2

    return stepLog[x] if stepLog[x]<math.inf else -1

print(minimumJumps(forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], a = 29, b = 98, x = 80))
