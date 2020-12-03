# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    pre = None 
    len = 0
    check = False
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.root = head
        self.pre = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if self.check:
            node = self.root
            for i in range(randint(0,self.len-1)):
                node = node.next
            return node.val
              
        node = self.pre 
        loop = randint(1,100)
        for i in range(loop):
            node = node.next
            if not self.check: self.len += 1
            if not node:
                self.check = True 
                node = self.root
                
        self.pre = node
        return node.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
