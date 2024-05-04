class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        for index, char in enumerate(strs[0]):
            if char == strs[-1][index]:
                ans += char
            else:
                break
        return ans
