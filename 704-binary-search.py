class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
