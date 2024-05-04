class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) != len(set(nums)) else False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_dict = {}
        for num in nums:
            if num in unique_dict.keys():
                return True
            else:
                unique_dict[num] = 1
        return False
