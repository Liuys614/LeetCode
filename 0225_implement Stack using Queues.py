class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        b = deque([x])
        b += self.a
        self.a = b

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.a.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.a[0] 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.a 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
