class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        substring = 0
        s_pos, t_pos = 0, 0
        while t_pos < len(t) and s_pos < len(s):
            if s[s_pos] == t[t_pos]:
                substring += 1
                s_pos += 1
                t_pos += 1
            else:
                s_pos += 1
        return len(t) - substring
