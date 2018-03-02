/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode RotateRight(ListNode head, int k) {
        if( k == 0 ){
            return head;
        }
        
        // Get List length
        int ListLength = 0;
        ListNode NodePtr = head;
        while( NodePtr != null ){
            NodePtr = NodePtr.next;
            ListLength++;
        }
        
        // optimization
        if( ListLength > 0 ){
            k = k % ListLength;
        }
        
        // Rotate List
        for( int i = 0; i < k; i++ ){
            head = RotateRight( head );
        }

        return head;
    }
    
    public ListNode RotateRight( ListNode head ){
        if( head == null || head.next == null ){
            return head;
        }
        
        ListNode NodeBeforeTailPtr = head;
        ListNode TailPtr = head.next;
        
        while( TailPtr.next != null ){
            NodeBeforeTailPtr = NodeBeforeTailPtr.next;
            TailPtr = TailPtr.next;
        }

        NodeBeforeTailPtr.next = null;
        TailPtr.next = head;
        
        return TailPtr;
    }
}
