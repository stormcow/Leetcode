class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = [num for row in vec for num in row]
        self.current_index = 0

    def next(self) -> int:
        num = self.vec[self.current_index]
        self.current_index += 1
        return num

    def hasNext(self) -> bool:
        return len(self.vec) > self.current_index


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
