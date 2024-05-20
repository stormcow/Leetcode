class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        powerset = []
        for r in range(1, len(nums) + 1):
            powerset.extend(list(itertools.combinations(nums, r)))

        answer = 0
        for set in powerset:
            answer += functools.reduce(lambda acc, curr: acc ^ curr, set, 0)
        return answer
