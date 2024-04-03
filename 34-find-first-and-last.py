class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), len(nums) - 1 - nums[::-1].index(target)]
        except ValueError:
            return [-1, -1]
