class MinStack:

    def __init__(self):
        self.items = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.min:
            self.min.append(val)
        elif self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self) -> None:
        if self.items:
            self.items.pop()
            self.min.pop()

    def top(self) -> int:
        if self.items:
            return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]