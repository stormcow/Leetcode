class TwoSum:
    def __init__(self):
        self.numbers = []

    def add(self, number: int) -> None:
        self.numbers.append(number)

    def find(self, value: int) -> bool:
        hash_t = {}
        for number in self.numbers:
            if (value - number) in hash_t:
                return True
            else:
                hash_t[number] = 0


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
