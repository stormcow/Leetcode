class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) > len(t):
            return False
        for char in s:
            if index == 0:
                index = t.find(char)
            else:
                index = t.find(char, index + 1)
            if index == -1:
                return False
        return True
