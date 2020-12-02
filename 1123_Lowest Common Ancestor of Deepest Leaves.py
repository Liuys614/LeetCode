# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode) -> (int, TreeNode):
        if not node:
            return 0, None 
        
        l, ln = self.dfs(node.left)
        r, rn = self.dfs(node.right)
        
        if l > r:
            return l+1, ln
        elif r > l:
            return r+1, rn
        else:
            return l+1, node
            
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[1]
