class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in t:
                s.replace(s[i], '')
                t.replace(s[i], '')

        if len(s) == 0  and len(t) == 0:
            return True

        return False        
