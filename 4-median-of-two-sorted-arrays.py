class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        arr_len = len(arr)
        mid = int(arr_len / 2)
        if arr_len % 2 == 1:
            return arr[mid]
        return (arr[mid] + arr[mid - 1]) / 2
