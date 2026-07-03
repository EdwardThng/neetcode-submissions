class Node:

    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        if self.node.next is not None:
            self.node.next.prev = None
            self.node.next = None
        self.node.next = Node(url)
        self.node.next.prev = self.node
        self.node = self.node.next

    def back(self, steps: int) -> str:
        if self.node.prev is not None:
            while self.node.prev != None and steps > 0:
                self.node = self.node.prev
                steps -= 1
            return self.node.url
        else:
            return self.node.url

    def forward(self, steps: int) -> str:
        if self.node.next is not None:
            while self.node.next != None and steps > 0:
                self.node = self.node.next
                steps -= 1
            return self.node.url
        else:
            return self.node.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)