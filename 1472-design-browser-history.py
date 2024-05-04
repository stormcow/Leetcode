class DoubleList:
    def __init__(self, val, prev, next_n):
        self.val = val
        self.prev = prev
        self.next_n = next_n


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = DoubleList(homepage, None, None)

    def visit(self, url: str) -> None:
        self.head.next_n = DoubleList(url, self.head, None)
        self.head = self.head.next_n

    def back(self, steps: int) -> str:
        while steps != 0 and self.head.prev is not None:
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps != 0 and self.head.next_n is not None:
            self.head = self.head.next_n
            steps -= 1
        return self.head.val
