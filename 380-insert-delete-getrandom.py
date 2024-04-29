import random


class RandomizedSet:
    def __init__(self):
        self._dct = {}
        self._lst = []

    def insert(self, val: int) -> bool:
        if self._dct.get(val, -1) == -1:
            self._lst.append(val)
            index = len(self._lst) - 1
            self._dct[val] = index
            return True
        return False

    def remove(self, val: int) -> bool:
        index = self._dct.get(val, -1)
        if index == -1:
            return False
        tmp_val = self._lst[-1]
        self._lst[-1] = self._lst[index]
        self._lst[index] = tmp_val
        self._dct[tmp_val] = index
        self._lst.pop()
        self._dct.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self._lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
