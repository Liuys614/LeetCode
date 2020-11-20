# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.dict = {}
        
        def dfs(node:TreeNode) -> List[int]:
            if not node:
                return []
            #print(f"node:{node.val}")
            l = dfs(node.left)
            r = dfs(node.right)
            len_l = len(l)
            len_r = len(r)
            if len_l >= len_r:
                s = [node.val] + [max(v,l[i]) for i,v in enumerate(r)]
                if l:
                    s += l[len_r:]
            else:
                s = [node.val] + [max(v,r[i]) for i,v in enumerate(l)]
                if r:
                    s += r[len_l:]
            #print(s)
            return s
        return dfs(root)


