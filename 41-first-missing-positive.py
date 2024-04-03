class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = list(filter(lambda x: x > 0, sorted(nums)))
        if len(l) == 0 or l[0] > 1:
            return 1
        for i in range(len(l)):
            if i + 1 < len(l) and l[i + 1] - l[i] > 1:
                return l[i] + 1
        return l[-1] + 1
