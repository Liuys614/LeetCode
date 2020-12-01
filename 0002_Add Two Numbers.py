# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res, resptr, carry, l1ptr, l2ptr = None, None, 0, l1, l2
        
        while l1ptr or l2ptr:
            sum = (l1ptr.val if l1ptr else 0 ) + (l2ptr.val if l2ptr else 0) + carry
            carry = sum//10
            if not res:
                res = ListNode(sum%10, None)
                resptr = res
            else:
                resptr.next = ListNode(sum%10, None)
                resptr = resptr.next 
            l1ptr = l1ptr.next if l1ptr else None
            l2ptr = l2ptr.next if l2ptr else None
            
        if carry:
            resptr.next = ListNode(carry, None)
        return res 



