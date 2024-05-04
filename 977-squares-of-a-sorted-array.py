class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                nums[left]=nums[left] ** 2)
                left += 1
            else:
                nums[right]= nums[right] ** 2)
                right -= 1
        return nums
