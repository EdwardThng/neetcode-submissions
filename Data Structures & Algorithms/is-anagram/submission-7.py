class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] not in hashmap1:
                hashmap1[s[i]] = 1
            else:
                hashmap1[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in hashmap2:
                hashmap2[t[j]] = 1
            else:
                hashmap2[t[j]] += 1
        
        return hashmap1 == hashmap2