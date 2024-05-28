class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        longest = 0
        l = 0
        currCost = 0
        for i in range(len(s)):
            difference = abs(ord(s[i]) - ord(t[i]))
            currCost += difference
            while currCost > maxCost:
                currCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            longest = max(longest, i - l + 1)
        return longest
