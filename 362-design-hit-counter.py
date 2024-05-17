class HitCounter:
    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        self.hits[timestamp] = self.hits.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        sum = 0
        for i in range(max(0, timestamp - 300) + 1, timestamp + 1):
            sum += self.hits.get(i, 0)
        return sum


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
