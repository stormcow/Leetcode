class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_val = 0
        l, r = 0, 1
        while l < r:
            sum_val += abs(ord(s[l]) - ord(s[r]))
            l += 1
            r = r + 1 if r < len(s) - 1 else r

        return sum_val
