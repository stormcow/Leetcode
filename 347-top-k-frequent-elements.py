class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        lst = [*hash_map.items()]
        heapq.heapify(lst)

        return [val[0] for val in heapq.nlargest(k, lst, key=lambda x: x[1])]
