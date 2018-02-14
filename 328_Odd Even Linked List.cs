/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode OddEvenList(ListNode head) {
        if( head == null || head.next == null ){
            return head;
        }
        
        ListNode OddHead = head;
        ListNode EvenHead = head.next;
        ListNode OddTail = head;
        ListNode EvenTail = head.next;
        ListNode CurNode = (head.next).next;
        OddTail.next = null;
        EvenTail.next = null;
        
        int nIndex = 3;
        
        while( CurNode != null )
        {
            if( nIndex % 2 ==0 ){
                EvenTail.next = CurNode;
                CurNode = CurNode.next;
                EvenTail = EvenTail.next;
                EvenTail.next = null;
            }
            else{
                OddTail.next = CurNode;
                CurNode = CurNode.next;
                OddTail = OddTail.next;
                OddTail.next = null;
            }
            nIndex++;
        }
        
        OddTail.next = EvenHead;
        return OddHead;
    }
}