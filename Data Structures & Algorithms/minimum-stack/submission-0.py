class MinStack:

    def __init__(self):
        self.items = []
        
    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        if self.items:
            self.items.pop()

    def top(self) -> int:
        if self.items:
            return self.items[-1]

    def getMin(self) -> int:
        if self.items:
            arr = set(self.items)
            return min(arr)

