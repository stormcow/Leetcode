class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False


# i cry
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            if hash_s.get(s[i], -1) != -1:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
            if hash_t.get(t[i], -1) != -1:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        return hash_s == hash_t
