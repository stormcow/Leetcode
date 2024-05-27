class Solution:
    def specialArray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        for index, val in enumerate(sorted_nums):
            slice_len = len(sorted_nums[index:])
            if index == 0:
                if slice_len <= val:
                    return slice_len
            else:
                if slice_len <= val and slice_len > sorted_nums[index - 1]:
                    return slice_len
        return -1
