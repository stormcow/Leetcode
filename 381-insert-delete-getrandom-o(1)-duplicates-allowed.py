class RandomizedCollection:
    def __init__(self):
        self.indexes = {}
        self.values = []

    def insert(self, val: int) -> bool:
        self.values.append(val)
        index = len(self.values) - 1
        if val in self.indexes:
            self.indexes[val].append(index)
            return False
        else:
            self.indexes[val] = deque([index])
            return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        else:
            index = self.indexes[val].pop()
            if index > len(self.values) - 1:
                index = len(self.values) - 1
            if len(self.indexes[val]) == 0:
                self.indexes.pop(val)
            if index == len(self.values) - 1:
                self.values.pop()
            else:
                tmp_val = self.values[-1]
                self.values[-1] = self.values[index]
                self.values[index] = tmp_val
                self.values.pop()
                new_index = self.indexes[tmp_val].popleft()
                new_index = index
                self.indexes[tmp_val].append(new_index)
            return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
