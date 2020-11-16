/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        ListNode curNodePtr = head;
        
        while( true ){
            // break while left one Node
            if( curNodePtr == null || curNodePtr.next == null ){
                break;
            }
            
            int nCurVal = curNodePtr.val;
            int nNextVal = curNodePtr.next.val;
            
            curNodePtr.val = nNextVal;
            curNodePtr.next.val = nCurVal;
            
            curNodePtr = curNodePtr.next.next;
        }
        
        return head;
    }
}
