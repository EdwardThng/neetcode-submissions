class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_srt = "".join(sorted(s))
        t_srt = "".join(sorted(t))
        if s_srt == t_srt:
            return True
        return False