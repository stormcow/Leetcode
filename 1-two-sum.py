class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            tmp = target - val
            try:
                return [index, nums.index(tmp, index + 1)]
            except ValueError:
                continue
