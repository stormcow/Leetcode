# 1st solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if hash_map.get(sorted_word, -1) != -1:
                hash_map[sorted_word] += [word]
            else:
                hash_map[sorted_word] = [word]

        return hash_map.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            hash_map[tuple(count)].append(word)

        return hash_map.values()
