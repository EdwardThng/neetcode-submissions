class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashmap1[s[i]] = 0
        for j in range(len(s)):
            hashmap1[s[j]] += 1
        
        for i in range(len(t)):
            hashmap2[t[i]] = 0
        for j in range(len(t)):
            hashmap2[t[j]] += 1

        for key in hashmap1:
            if key not in hashmap2:
                return False
            if hashmap1[key] != hashmap2[key]:
                return False 

        return True

        
                
