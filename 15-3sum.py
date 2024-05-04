class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if (first + nums[left] + nums[right]) < 0:
                    left += 1
                elif (first + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    sums.append([first, nums[left], nums[right]])
                    left += 1
                    while left != right and nums[left] == nums[left - 1]:
                        left += 1
        return sums
