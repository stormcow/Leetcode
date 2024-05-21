class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []
        for r in range(len(nums) + 1):
            powerset.extend(list(itertools.combinations(nums, r)))
        return powerset
