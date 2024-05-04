class DoubleLinkedList:
    def __init__(self, val, prev, next_n):
        self.val = val
        self.prev = prev
        self.next_n = next_n


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = DoubleLinkedList(homepage, None, None)

    def visit(self, url: str) -> None:
        self.head = DoubleLinkedList(url, self.head, None)

    def back(self, steps: int) -> str:
        while steps != 0 and self.head.prev is not None:
            tmp_pointer = self.head
            self.head = self.head.prev
            self.head.next_n = tmp_pointer
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps != 0 and self.head.next_n is not None:
            tmp_pointer = self.head
            self.head = self.head.next_n
            self.head.prev = tmp_pointer
            steps -= 1
        return self.head.val
