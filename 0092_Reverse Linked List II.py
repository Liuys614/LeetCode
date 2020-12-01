# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        i = 1
        root = ListNode()
        root.next = head 
        pre, cur, next = root, head, head.next
        tmpHead, tmpTail = None, None
        
        while i <= n and n!=m:
            if i == m:
                tmpHead = pre 
                tmpTail = cur 
            elif m < i < n:
                cur.next = pre
            elif i == n:
                tmpHead.next = cur
                tmpTail.next = next
                cur.next = pre 
                break
                
            pre = cur
            cur = next
            next = next.next
            i += 1
                
        return root.next 
