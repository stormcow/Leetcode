class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        chars1 = [*word1[::-1]]
        chars2 = [*word2[::-1]]
        while chars1:
            res += chars1.pop()
            if not chars2:
                res += chars1[::-1]
                break
            res += chars2.pop()
        if chars2:
            res += chars2[::-1]
        return "".join(res)
