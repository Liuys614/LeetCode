"""
# BFS解法

## 資料結構：
使用python的deque來模擬queue的資料結構
右邊塞入要走的node，左邊取出node，做到整個deque空了為止
deque裡面放了三個東西：node, 來的方向, 目前連到這個位置的長度

## 優化的部分：
1. 不塞入空的node。
2. 當從右邊來的時候，不會把左邊的當成頭，一定會讓他接續計算上方的長度。

## 每個node拿到之後要做的事情：
1. 判斷是否可以接續往下的node，有的話更新path長度並塞入deque
2. 判斷是否有可以重新開始的node，可以的話塞入deque
3. 更新最大值

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        deq = deque()
        max_path = 0

        if root.left: 
            deq.append((root.left,"l",1))
        if root.right:
            deq.append((root.right,"r",1))

        while deq:
            node, d, p = deq.popleft()
            if node.left:
                if d == "r":
                    deq.append((node.left, "l", p+1))
                else:
                    deq.append((node.left, "l", 1))
            if node.right:
                if d == "l":
                    deq.append((node.right, "r", p+1))
                else:
                    deq.append((node.right, "r", 1))
            max_path = max(max_path, p)
            
        return max_path
