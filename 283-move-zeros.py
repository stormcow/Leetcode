class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for num in nums[:]:
            if num == 0:
                zeros.append(num)
                nums.remove(num)
        nums.extend(zeros)
