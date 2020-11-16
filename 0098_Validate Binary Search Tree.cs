/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public bool IsValidBST(TreeNode root) {
        return IsValidBST( root, Int64.MaxValue, Int64.MinValue );
    }

    public bool IsValidBST( TreeNode root, long nMax, long nMin ){
        if( root == null ){
            return true;
        }
        
        if( root.left != null ){
            if( root.left.val <= nMin || root.left.val >= root.val ){
                return false;
            }
        }
        
        if( root.right != null ){
            if( root.right.val >= nMax || root.right.val <= root.val ){
                return false;
            }
        }
        
        if( IsValidBST( root.left, root.val, nMin ) == false ){
            return false;
        }
        
        if( IsValidBST( root.right, nMax, root.val ) == false ){
            return false;
        }
        
        return true;
    }
}
