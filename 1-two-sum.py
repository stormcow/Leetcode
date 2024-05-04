# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, val in enumerate(nums):
            tmp = target - val
            try:
                return [index, nums.index(tmp, index + 1)]
            except ValueError:
                continue


# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for index, val in enumerate(nums):
            if target - val in vals:
                return [index, vals[target - val]]
            else:
                vals[val] = index
