class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = sorted(nums)
        for i in range(0, len(nums), 2):
            try:
                if l[i - 1] == l[i] or l[i + 1] == l[i]:
                    return l[i]
            except ValueError:
                continue
