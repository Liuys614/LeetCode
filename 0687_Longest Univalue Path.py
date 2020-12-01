

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        return max(self.dfs(root), self.res)

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0

        lp, rp = 0, 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)

        if node.left and node.left.val == node.val:
            lp = l + 1
            self.res = max(lp, self.res)

        if node.right and node.right.val == node.val:
            rp = r + 1
            self.res = max(rp, self.res)

        if node.left and node.right and node.left.val == node.val == node.right.val:
            self.res = max(l+r+2, self.res)

        return max(lp, rp)



