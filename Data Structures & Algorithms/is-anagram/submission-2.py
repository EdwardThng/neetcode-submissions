class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in hashmap2:
                hashmap2[t[i]] = 1
            else:
                hashmap2[t[i]] += 1
        
        for keys in hashmap:
            if keys in hashmap2:
                if hashmap[keys] == hashmap2[keys]:
                    hashmap2.pop(keys)
            else:
                return False
        
        if len(hashmap2) == 0:
            return True

        return False
