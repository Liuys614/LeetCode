# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.array = []
        self.maxLen = 0
        
        def dfs(node:TreeNode,lv:int):
            if not node:
                return
            if lv == self.maxLen:
                self.array.append(node.val)
                self.maxLen += 1
            else:
                self.array[lv] = max(self.array[lv], node.val)
            dfs(node.left,lv+1)
            dfs(node.right,lv+1)        
                
        dfs(root,0)
        return self.array
