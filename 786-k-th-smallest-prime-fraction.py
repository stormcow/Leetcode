class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lst = []
        heapq.heapify(lst)
        l, r = 0, len(arr) - 1
        c = k if k <= len(arr) else len(arr)
        while c > 0:
            if l == r:
                l = 0
                r -= 1
                c -= 1
            else:
                heapq.heappush(lst, (arr[l] / arr[r], [arr[l], arr[r]]))
                l += 1
        while k > 0 and lst:
            ans = heapq.heappop(lst)
            k -= 1
        return ans[1]
