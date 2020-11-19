# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node:TreeNode, sum: int) -> (List[int],int):
            if not node:
                return ([],0)
            sum_l, cnt_l= dfs(node.left,sum)
            sum_r, cnt_r= dfs(node.right,sum)
            sum_c = [node.val] + [ x+node.val for x in sum_l] + [ x+node.val for x in sum_r] 
            cnt_c = sum_c.count(sum) + cnt_l + cnt_r 
            return (sum_c, cnt_c)
            
        return dfs(root, sum)[1] 



