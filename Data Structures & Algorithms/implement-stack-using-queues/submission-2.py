from collections import deque

class MyStack:

    def __init__(self):
        self.deque1 = deque()
        self.deque2 = deque()

    def push(self, x: int) -> None:
        self.deque1.append(x)

    def pop(self) -> int:
        while len(self.deque1) != 1:
            self.deque2.append(self.deque1.popleft())
        top = self.deque1.pop()
        self.deque1, self.deque2 = self.deque2, self.deque1
        return top

    def top(self) -> int:
        while len(self.deque1) != 1:
            self.deque2.append(self.deque1.popleft())
        top = self.deque1.pop()
        self.deque2.append(top)
        self.deque1,self.deque2 = self.deque2, self.deque1
        return top

    def empty(self) -> bool:
        if len(self.deque1) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()