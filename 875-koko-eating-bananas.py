class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        count_max = r

        while l <= r:
            mid = (l + r) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile / mid)
            if count <= h:
                count_max = min(count_max, mid)
                r = mid - 1
            else:
                l = mid + 1
        return count_max
