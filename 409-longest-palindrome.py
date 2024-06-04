class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        even = [0]
        uneven = [0]
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        for key, value in hash_map.items():
            if value % 2 == 0:
                even.append(value)
            else:
                uneven.append(value)
        max_uneven = max(uneven)
        uneven.remove(max_uneven)
        uneven = [number - 1 for number in uneven if number > 1]
        return sum(even) + sum(uneven) + max_uneven
